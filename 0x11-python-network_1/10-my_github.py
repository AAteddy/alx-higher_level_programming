#!/usr/bin/python3
"""Uses the GitHub API to display a GitHub ID based on given credentials.

Usage: ./10-my_github.py <GitHub username> <GitHub password>
  - Uses Basic Authentication to access the ID.
"""

import sys
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    usrname = sys.argv[1]
    passwrd = sys.argv[2]
    auth = HTTPBasicAuth(usrname, passwrd)

    r = requests.get("https://api.github.com/user", auth=auth)

    print(r.json().get("id"))
