#!/bin/bash
# A bashscript that takes in a URL
# sends a GET request to the URL,
# Displays the size of the body of the response

curl -sL "$1"

