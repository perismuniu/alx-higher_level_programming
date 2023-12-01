#!/usr/bin/python3
"""
A Python script that takes a URL and an email, sends a POST request,
and displays the body of the response.
"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit("Usage: ./6-post_email.py <URL> <email>")

    url = sys.argv[1]
    email = sys.argv[2]

    payload = {'email': email}
    response = requests.post(url, data=payload)

    print("Your email is:", response.text)
