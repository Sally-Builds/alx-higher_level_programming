#!/bin/bash
# Send a request to an endpoint and displays the response size

curl -s -w "%{size_download}\n" -o /dev/null $1 
