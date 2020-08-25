#!/usr/bin/python3
"""
Please list 10 commits (from the most recent to oldest) of the repository
“rails” by the user “rails”
"""
import requests
from sys import argv


if __name__ == "__main__":
    url = 'https://api.github.com/repos/'\
                     + argv[2] + '/' + argv[1] + '/commits'
    response = requests.get(url)
    if "json" not in response.headers.get('content-type'):
        print("Not a valid JSON")
    else:
        json_obj = response.json()
        i = 0
        for res in json_obj:
            if i > 10:
                break
            print(res.get('sha') + ': ', end="")
            print(res.get('commit').get('author').get('name'))
            i += 1
