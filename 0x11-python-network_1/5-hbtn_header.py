#!/usr/bin/python3
"""
A Python script that takes a URL, sends a request, and displays
the value of X-Request-Id in the response header.
"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("Usage: ./5-hbtn_header.py <URL>")

    url = sys.argv[1]

    response = requests.get(url)

    x_request_id = response.headers.get('X-Request-Id')
    print(x_request_id)
