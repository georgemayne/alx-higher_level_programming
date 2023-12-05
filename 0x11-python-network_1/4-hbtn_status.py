#!/usr/bin/python3
"""
script that fetches https://alx-intranet.hbtn.io/status
"""
import requests

if __name__ == '__main__':
    ind = requests.get('https://alx-intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type: {}".format(ind.text.__class__))
    print("\t- content: {}".format(ind.text))
