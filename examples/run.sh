#!/bin/bash

# Exit on any error
set -e

# Function to cleanup on exit or interrupt
cleanup() {
    echo "Cleaning up..."
    docker stop lsproxy 2>/dev/null || true
    exit
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
            cleanup
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
        python3 -m venv "$VENV_DIR"
        source "$VENV_DIR/bin/activate"
        
        # Update pip
        python -m pip install --upgrade pip
        # Install requirements
        if [ -f "requirements.txt" ]; then
            echo "Installing requirements from requirements.txt..."
            pip install -r requirements.txt
        else
            echo "Requirements file not found"
            exit 1
        fi
        echo "Virtual environment setup completed!"
    else
        echo "Using existing virtual environment..."
        source "$VENV_DIR/bin/activate"
    fi
}

# Set up trap for SIGINT (Ctrl+C) and SIGTERM
trap cleanup SIGINT SIGTERM

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

# Setup and activate virtual environment
setup_venv

# Start docker container
echo "Starting docker container..."
docker run --rm -d -p 4444:4444 -v $1:/mnt/workspace --name lsproxy agenticlabs/lsproxy:0.1.0a1

# Show logs in background
docker logs -f lsproxy &

# Wait for server to be ready
wait_for_server

# Run the code graph
echo "Running example..."
marimo run $SCRIPT_DIR/code_graph/code_graph.py
