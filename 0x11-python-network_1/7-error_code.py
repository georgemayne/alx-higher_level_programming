#!/usr/bin/python3
"""script that takes in a URL
- sends a request to the URL
"""
import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]

    ind = requests.get(url)
    if ind.status_code >= 400:
        print("Error code: {}".format(ind.status_code))
    else:
        print(ind.text)
