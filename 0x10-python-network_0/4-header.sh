#!/bin/bash
# script that takes in a URL displays all HTTP methods the server will accept.
curl -s-X GET "$1" -H "X-School-User-Id: 98"
