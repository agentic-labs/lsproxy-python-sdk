#!/bin/bash

# Exit on any error
set -e

# Global variable for virtual environment path
SCRIPT_DIR=""
VENV_DIR=""

# Function to cleanup docker and processes
cleanup_docker() {
    # Disable the trap temporarily to prevent recursive triggers
    trap "" SIGINT SIGTERM

    echo "Starting cleanup process..."

    # Kill any background processes (like docker logs)
    pkill -P $$ || true

    echo "Stopping docker container..."
    docker stop lsproxy 2>/dev/null || true

    # Add a small delay to ensure docker has time to stop
    sleep 2

    # Double-check if container still exists and force kill if necessary
    if docker ps -q -f name=lsproxy | grep -q .; then
        echo "Container still running, forcing removal..."
        docker kill lsproxy 2>/dev/null || true
    fi

    echo "Cleanup completed"
    kill -9 $$  # Force exit the script
}

# Function to cleanup virtual environment on failure
cleanup_venv() {
    # Disable the trap temporarily to prevent recursive triggers
    trap "" SIGINT SIGTERM

    if [ -n "$VENV_DIR" ] && [ -d "$VENV_DIR" ]; then
        echo "Cleaning up incomplete virtual environment..."
        rm -rf "$VENV_DIR"
        echo "Virtual environment cleanup completed"
    fi
    exit 1
}

# Function to check if server is ready using OpenAPI endpoint
wait_for_server() {
    echo "Waiting for server to be ready..."
    local max_attempts=30
    local attempt=1
    local endpoint="/api-docs/openapi.json"
    
    while true; do
        if [ $attempt -ge $max_attempts ]; then
            echo "Server failed to start after $max_attempts attempts"
            cleanup_docker
            exit 1
        fi
        
        # Temporarily disable exit on error for the curl command
        set +e
        response=$(curl -s -f http://localhost:4444${endpoint} 2>&1)
        curl_status=$?
        set -e
        
        if [ $curl_status -eq 0 ]; then
            # Temporarily disable exit on error for the jq check
            set +e
            if command -v jq >/dev/null 2>&1; then
                if echo "$response" | jq empty >/dev/null 2>&1; then
                    echo "Server is ready! (OpenAPI endpoint accessible)"
                    break
                else
                    echo "Attempt $attempt: Invalid JSON response"
                fi
            else
                # If jq isn't available, just check if we got a response
                echo "Server is ready! (OpenAPI endpoint accessible)"
                break
            fi
            set -e
        else
            echo "Attempt $attempt: Server not ready yet..."
        fi
        
        sleep 4 
        ((attempt++))
    done
}

# Function to setup virtual environment
setup_venv() {
    SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
    VENV_DIR="$SCRIPT_DIR/venv"
    
    # Change to script directory before doing anything else
    cd "$SCRIPT_DIR"
    
    # Check if Python is installed
    if ! command -v python3 &> /dev/null; then
        echo "Python3 is required but not installed. Please install Python3 first."
        exit 1
    fi 

    # Create virtual environment if it doesn't exist
    if [ ! -d "$VENV_DIR" ]; then
        echo "Setting up virtual environment..."
        # Remove any partially created venv directory
        rm -rf "$VENV_DIR"
        
        echo "Creating virtual environment..."
        {
            python3 -m venv "$VENV_DIR" && \
            source "$VENV_DIR/bin/activate" && \
            # Update pip
            python -m pip install --upgrade pip && \
            # Check for requirements.txt
            if [ ! -f "requirements.txt" ]; then
                echo "Requirements file not found"
                cleanup_venv
                exit 1
            fi && \
            # Install requirements
            echo "Installing requirements from requirements.txt..." && \
            pip install -r requirements.txt
        } || {
            # If any command in the chain fails
            echo "Failed to setup virtual environment"
            cleanup_venv
            exit 1
        }
        echo "Virtual environment setup completed!"
    else
        echo "Using existing virtual environment..."
        source "$VENV_DIR/bin/activate"
    fi
}

# Check if argument is provided
if [ $# -ne 1 ]; then
    echo "Usage: $0 /absolute/path/to/code"
    exit 1
fi

# Check if path is absolute
if [[ "$1" != /* ]]; then
    echo "Error: Please provide an absolute path"
    exit 1
fi

# Set initial trap for venv cleanup
trap 'cleanup_venv' SIGINT SIGTERM EXIT

# Setup and activate virtual environment
setup_venv

# Update trap for docker cleanup now that venv is setup
trap 'cleanup_docker' SIGINT SIGTERM EXIT

# Start docker container
echo "Starting docker container..."
docker run --rm -d -p 4444:4444 -v "$1":/mnt/workspace --name lsproxy agenticlabs/lsproxy:0.1.0a1

# Show logs in background
docker logs -f lsproxy &

# Wait for server to be ready
wait_for_server

# Run the code graph
echo "Running example..."
marimo edit $SCRIPT_DIR/code_graph/code_graph.py
