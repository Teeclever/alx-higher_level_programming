#!/bin/bash
# Bash script that takes in a URL as an argument, sends a GET request to the URL, and displays the body of the response. A header variable X-School-User-Id must be sent with the value 98, Usage: ./4-header.sh 0.0.0.0:5000/route_5 ; echo ""
curl -s -H "X-School-User-Id":98 "$1"
