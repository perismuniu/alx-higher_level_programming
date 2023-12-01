#!/usr/bin/python3
"""
A Python script that takes a letter, sends a POST request,
and displays the result based on the response body.
"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) == 1:
        q = ""
    else:
        q = sys.argv[1]

    payload = {'q': q}
    url = 'http://0.0.0.0:5000/search_user'

    try:
        response = requests.post(url, data=payload)
        data = response.json()

        if data:
            print("[{}] {}".format(data['id'], data['name']))
        else:
            print("No result")

    except ValueError:
        print("Not a valid JSON")
