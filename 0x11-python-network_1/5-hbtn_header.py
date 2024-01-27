#!/usr/bin/python3

"""Python script that takes in a URL, sends a request to the URL
and displays the value of the variable X-Request-Id in the response header.
Usage: ./5-hbtn_header.py <URL>
"""

import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]

    url_req = requests.get(url)
    print(url_req.headers.get("X-Request-Id"))
