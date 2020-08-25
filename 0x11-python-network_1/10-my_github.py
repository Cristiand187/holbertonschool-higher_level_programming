#!/usr/bin/python3

"""
Write a Python script that takes your Github credentials
(username and password) and
uses the Github API to display your id
"""
import requests
from sys import argv


if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    response = requests.get('https://api.github.com/user',
                            auth=(username, password))
    if "json" not in response.headers.get('content-type'):
        print("Not a valid JSON")
    else:
        json_res = response.json()
        print(json_res.get('id'))
