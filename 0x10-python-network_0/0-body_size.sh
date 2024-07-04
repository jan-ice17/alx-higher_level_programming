#!/bin/bash
# A bashscript that takes in a URl 
curl -sI "$1" | grep -i Content-Length | awk '{print $2}'
