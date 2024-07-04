#!/bin/bash
# script that takes in a URL displays all HTTP methopt.
curl -s -X GET "$1" -H "X-School-User-Id: 98"
