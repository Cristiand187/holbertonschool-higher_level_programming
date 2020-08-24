#!/usr/bin/python3
"""sends a POST request to the passed URL with the email as a parameter"""
from urllib.request import Request, urlopen
from urllib.parse import urlencode
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    email = {'email': argv[2]}

    data = urlencode(email)
    data = data.encode('ascii')
    with urlopen(url, data) as response:
        the_page = response.read()
        print(the_page.decode('utf-8'))
