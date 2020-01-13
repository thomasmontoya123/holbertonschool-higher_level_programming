#!/usr/bin/python3
'''uses the Github API to display your id'''
if __name__ == "__main__":
    import requests
    import sys

    url = "https://api.github.com/user"
    result = requests.get(url, auth=(sys.argv[1], sys.argv[2]))
    print(result.json().get("id"))
