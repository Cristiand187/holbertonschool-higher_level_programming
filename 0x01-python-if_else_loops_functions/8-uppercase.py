#!/usr/bin/python3
def uppercase(str):
    for l in str:
        c = ord(l)
        if (97 <= c <= 122):
            c = c - 32
        print("{:c}".format(c), end="")
    print(end="\n")
