#!/usr/bin/python3
for alp in range(97, 123):
    if (chr(alp) != "e" and chr(alp) != "q"):
        print("{:c}".format(alp), end="")
