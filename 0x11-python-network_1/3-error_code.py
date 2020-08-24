#!/usr/bin/python3
"""
 script that takes in a URL, sends a request to the URL and
 displays the body of the response (decoded in utf-8).
"""
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
from sys import argv


if __name__ == "__main__":
    req = Request(argv[1])
    try:
        with urlopen(req) as response:
            the_page = response.read()
            print(the_page.decode('utf-8'))
    except HTTPError as e:
        error_code = str(e).split(' ')[2][:-1]
        print("Error code: " + str(error_code))
    except URLError as e:
        print('Reason: ', e.reason)
