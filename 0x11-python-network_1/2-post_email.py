#!/usr/bin/python3
"""
A Python script that takes a URL and an email, sends a POST request,
and displays the body of the response.
"""

import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit("Usage: ./2-post_email.py <URL> <email>")

    url = sys.argv[1]
    email = sys.argv[2]

    data = urllib.parse.urlencode({'email': email}).encode('utf-8')

    with urllib.request.urlopen(url, data=data) as response:
        body = response.read().decode('utf-8')
        print(body)
