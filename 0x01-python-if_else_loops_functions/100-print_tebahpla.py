#!/usr/bin/python3
alp = 122
while (alp != 96):
    if (alp % 2 == 0):
        print("{:c}".format(alp), end="")
    else:
        print("{:c}".format(alp - 32), end="")
    alp = alp - 1
