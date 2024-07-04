#!/bin/bash
# Write a Bash script that sends a JSON POST request to a URL passed as the first arg
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
