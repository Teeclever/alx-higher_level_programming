#!/usr/bin/python3

"""Python script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id
password in this case would be a personal access token
Usage: ./10-my_github.py <GitHub username> <GitHub password>
  - Uses Basic Authentication to access the ID.
"""
import sys
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    auth = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    request = requests.get("https://api.github.com/user", auth=auth)
    print(request.json().get("id"))
