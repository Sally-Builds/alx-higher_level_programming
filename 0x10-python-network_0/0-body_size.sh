#!/bin/bash
# Send a request to an endpoint and displays the response size
curl -sI "$1" | awk '/Content-Length/{print $2}'
