#!/usr/bin/python3
"""script that displays the value of the variable X-Request-Id
"""
import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]

    ind = requests.get(url)
    print(ind.headers.get("X-Request-Id"))
