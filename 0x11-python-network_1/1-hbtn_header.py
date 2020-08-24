#!/usr/bin/python3
"""sends a request to the URL and displays the value of the X-Request-Id"""
import urllib.request
from sys import argv


url = argv[1]
req = urllib.request.Request(url)
with urllib.request.urlopen(req) as response:
    print(response.headers.get('X-Request-Id'))
