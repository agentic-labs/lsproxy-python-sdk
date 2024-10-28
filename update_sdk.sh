#!/bin/bash

set -e

# Check if OpenAPI Generator is installed
if ! command -v openapi-generator &> /dev/null; then
    echo "OpenAPI Generator could not be found. Please install it first."
    exit 1
fi

# Run OpenAPI Generator with hardcoded values
echo "Generating SDK..."
openapi-generator generate \
    -i "openapi.json" \
    -g  python \
    --additional-properties=packageName=lsproxy \
    -o sdk

# Check if generation was successful
if [ $? -eq 0 ]; then
    echo "SDK generated successfully"
else
    echo "Failed to generate SDK. Please check the error messages above."
fi
