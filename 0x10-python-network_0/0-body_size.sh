#!/bin/bash

# Check if the URL argument is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Make a curl request to the URL and pipe the output to wc to count bytes
curl -sI "$1" | grep -i "content-length" | awk '{print $2}' | tr -d '\r'

