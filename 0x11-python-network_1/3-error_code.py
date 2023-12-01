#!/usr/bin/python3
"""
A Python script that takes a URL, sends a request,
and displays the body of the response.

Handles urllib.error.HTTPError exceptions and prints the HTTP status code.
"""

import urllib.request
import urllib.error
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("Usage: ./3-error_code.py <URL>")

    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            body = response.read().decode('utf-8')
            print(body)
    except urllib.error.HTTPError as e:
        print("Error code:", e.code)
