#!/usr/bin/python3
"""Lists 10 most recent commits on a given GitHub repository.
"""
import sys
import requests

if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(
        sys.argv[2], sys.argv[1])

    ind = requests.get(url)
    commits = ind.json()
    try:
        for g in range(10):
            print("{}: {}".format(
                commits[g].get("sha"),
                commits[g].get("commit").get("author").get("name")))
    except IndexError:
        pass
