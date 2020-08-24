#!/usr/bin/python3
"""Write a Python script that fetches https://intranet.hbtn.io/status"""
from urllib.request import Request, urlopen

req = Request('https://intranet.hbtn.io/status')
with urlopen(req) as response:
    html = response.read()
    print("Body response:")
    print("\t- type: {}".format(type(html)))
    print("\t- content: {}".format(html))
    print("\t- utf8 content: {}".format(html.decode('utf-8')))
