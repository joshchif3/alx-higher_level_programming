#!/bin/bash

# Script that takes in a URL, sends a GET request, and displays the body of the response

# Check if the URL argument is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Make a curl request to the URL and store response body in a temporary file
curl -s -o temp_body.txt "$1"

# Display the body of the response for a 200 status code
http_code=$(head -n 1 temp_body.txt | cut -d$' ' -f2)
if [ "$http_code" -eq 200 ]; then
    cat temp_body.txt
fi

# Clean up temporary file
rm -f temp_body.txt

