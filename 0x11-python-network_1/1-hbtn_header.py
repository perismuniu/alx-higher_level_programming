#!/usr/bin/python3
"""
A Python script that takes a URL, sends a request, and displays
the X-Request-Id variable from the response header.
"""

import urllib.request
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("Usage: ./1-hbtn_header.py <URL>")

    url = sys.argv[1]

    with urllib.request.urlopen(url) as response:
        header = response.getheader('X-Request-Id')
        print(header)
