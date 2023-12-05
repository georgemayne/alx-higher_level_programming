#!/usr/bin/python3
"""script that takes in a URL and an email address
- sends a POST request
"""
import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]
    value = {"email": sys.argv[2]}

    ind = requests.post(url, data=value)
    print(ind.text)
