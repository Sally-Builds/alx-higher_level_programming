#!/bin/bash
# Check if URL is provided as argument
if [ $# -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Send OPTIONS request to the URL and store the response
response=$(curl -s -X OPTIONS -i "$1")

# Extract and display the Allow header from the response
allow_header=$(echo "$response" | grep -i "Allow:")
if [ -n "$allow_header" ]; then
    echo "Allowed HTTP methods for $1:"
    echo "$allow_header" | sed 's/Allow: //i'
else
    echo "No Allow header found in the response."
fi

