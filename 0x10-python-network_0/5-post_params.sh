#!/bin/bash
# Bash script that takes in a URL, sends a POST request to the passed URL, and displays the body of the response. A variable `email` must be sent with the value `test@gmail.com`. A variable `subject` must be sent with the value `I will always be here for PLD`. Usage: ./5-post_params.sh 0.0.0.0:5000/route_6 ; echo ""
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
