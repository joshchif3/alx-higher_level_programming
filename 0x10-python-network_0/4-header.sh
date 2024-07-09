#!/bin/bash
# Script that takes in a URL, sends a GET request with a custom header, and displays the body of the response

# Check if the URL argument is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Make a curl request to the URL with custom header and store response body in a temporary file
curl -s -H "X-School-User-Id: 98" "$1"

# Ensure new line after output
echo ""

