#!/usr/bin/python3
"""
A Python script that takes a URL, sends a request, and displays
the body of the response.

Prints an error message if the HTTP status code is
greater than or equal to 400.
"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("Usage: ./7-error_code.py <URL>")

    url = sys.argv[1]

    response = requests.get(url)

    if response.status_code >= 400:
        print("Error code:", response.status_code)
    else:
        print(response.text)
