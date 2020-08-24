#!/usr/bin/python3
"""sends a request to the URL and displays the value of the X-Request-Id"""
from urllib.request import Request, urlopen
from sys import argv


url = argv[1]
req = Request(url)
with urlopen(req) as response:
    print(f.headers.get('X-Request-Id'))
