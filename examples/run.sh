#!/bin/bash

# Exit on any error
set -e

# Global variables
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
VENV_DIR="$SCRIPT_DIR/venv"

# Function to display basic usage message
show_usage() {
    echo "Usage: $(basename "$0") /absolute/path/to/code [--edit]"
    echo "Use -h or --help for more detailed information"
}

# Function to display detailed help message
show_help() {
    cat << EOF
Usage: $(basename "$0") /absolute/path/to/code [--edit] [--help]

A script to analyze code using marimo and lsproxy in a Docker container.

Arguments:
    /absolute/path/to/code   Absolute path to the code directory to analyze
                             This directory will be mounted in the Docker container

Options:
    --edit                   Launch marimo in edit mode instead of run mode
    -h, --help               Display this help message and exit

Description:
    This script sets up a Python virtual environment, launches an lsproxy Docker
    container, and runs a marimo code analysis graph. It handles:
    
    1. Virtual Environment Setup:
       - Creates a Python virtual environment if it doesn't exist
       - Installs required dependencies from requirements.txt
    
    2. Docker Container Management:
       - Launches an lsproxy container with the specified code mounted
       - Monitors container logs
       - Performs cleanup on exit
    
    3. Code Analysis:
       - Waits for the lsproxy server to be ready
       - Runs the code graph analysis using marimo
       - Supports both view-only (run) and interactive (edit) modes

Examples:
    $(basename "$0") /home/user/myproject          # Run in view mode
    $(basename "$0") /home/user/myproject --edit   # Run in edit mode
    $(basename "$0") --edit /home/user/myproject   # Same as above

Note:
    The script requires Python 3, Docker, and curl to be installed on the system.
    It will automatically clean up resources (Docker container, processes) on exit.
EOF
}

# Function to cleanup docker and processes
cleanup_docker() {
    trap "" SIGINT SIGTERM  # Prevent recursive triggers
    echo "Starting cleanup process..."
    pkill -P $$ || true
    docker stop lsproxy 2>/dev/null || true
    sleep 2
    if docker ps -q -f name=lsproxy | grep -q .; then
        echo "Container still running, forcing removal..."
        docker kill lsproxy 2>/dev/null || true
    fi
    echo "Cleanup completed"
    kill -9 $$
}

# Function to cleanup virtual environment on failure
cleanup_venv() {
    trap "" SIGINT SIGTERM  # Prevent recursive triggers
    if [ -n "$VENV_DIR" ] && [ -d "$VENV_DIR" ]; then
        echo "Cleaning up incomplete virtual environment..."
        rm -rf "$VENV_DIR"
        echo "Virtual environment cleanup completed"
    fi
    exit 1
}

# Function to check if server is ready
wait_for_server() {
    echo "Waiting for server to be ready..."
    local max_attempts=30
    local attempt=1
    
    while true; do
        if [ $attempt -ge $max_attempts ]; then
            echo "Server failed to start after $max_attempts attempts"
            cleanup_docker
            exit 1
        fi
        
        set +e
        response=$(curl -s -f http://localhost:4444/api-docs/openapi.json 2>&1)
        curl_status=$?
        set -e
        
        if [ $curl_status -eq 0 ]; then
            set +e
            if command -v jq >/dev/null 2>&1; then
                if echo "$response" | jq empty >/dev/null 2>&1; then
                    echo "Server is ready! (OpenAPI endpoint accessible)"
                    break
                fi
            else
                echo "Server is ready! (OpenAPI endpoint accessible)"
                break
            fi
            set -e
        fi
        
        echo "Attempt $attempt: Server not ready yet..."
        sleep 4 
        ((attempt++))
    done
}

# Function to setup virtual environment
setup_venv() {
    if ! command -v python3 &> /dev/null; then
        echo "Python3 is required but not installed. Please install Python3 first."
        exit 1
    fi

    cd "$SCRIPT_DIR"
    
    if [ ! -d "$VENV_DIR" ]; then
        echo "Setting up virtual environment..."
        rm -rf "$VENV_DIR"
        
        echo "Creating virtual environment..."
        {
            python3 -m venv "$VENV_DIR" && \
            source "$VENV_DIR/bin/activate" && \
            python -m pip install --upgrade pip && \
            if [ ! -f "requirements.txt" ]; then
                echo "Requirements file not found"
                cleanup_venv
                exit 1
            fi && \
            echo "Installing requirements from requirements.txt..." && \
            pip install -r requirements.txt
        } || {
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

# Parse command line arguments
EDIT_MODE=false
CODE_PATH=""

# Process all arguments
for arg in "$@"; do
    case "$arg" in
        --edit)
            EDIT_MODE=true
            ;;
        -h|--help)
            show_help
            exit 0
            ;;
        --*)
            echo "Unknown option: $arg"
            show_usage
            exit 1
            ;;
        *)
            if [ -z "$CODE_PATH" ]; then
                CODE_PATH="$arg"
            else
                echo "Error: Multiple paths specified"
                show_usage
                exit 1
            fi
            ;;
    esac
done

# Validate input
if [ $# -eq 0 ]; then
    show_usage
    exit 1
fi

if [ -z "$CODE_PATH" ]; then
    echo "Error: No path specified"
    show_usage
    exit 1
fi

if [[ "$CODE_PATH" != /* ]]; then
    echo "Error: Please provide an absolute path"
    show_usage
    exit 1
fi

# Main execution
trap 'cleanup_venv' SIGINT SIGTERM EXIT
setup_venv

trap 'cleanup_docker' SIGINT SIGTERM EXIT
echo "Starting docker container..."
docker run --rm -d -p 4444:4444 -v "$CODE_PATH":/mnt/workspace --name lsproxy agenticlabs/lsproxy:0.1.0a1

docker logs -f lsproxy &
wait_for_server

echo "Running example..."
if [ "$EDIT_MODE" = true ]; then
    marimo edit $SCRIPT_DIR/code_graph/code_graph.py
else
    marimo run $SCRIPT_DIR/code_graph/code_graph.py
fi
