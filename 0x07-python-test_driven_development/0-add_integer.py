#!/usr/bin/python3
"""My add integer"""


def add_integer(a, b=98):
    """This function sum two number

    Arguments:
        a {int} -- [number a]

    Keyword Arguments:
        b {int} -- [number b] (default: {98})

    Raises:
        ValueError: [a must be an integer]
        ValueError: [b must be an integer]
    """

    if (type(a) not in [float, int]):
        raise TypeError("a must be an integer")
    elif (type(b) not in [float, int]):
        raise TypeError("b must be an integer")
    else:
        return(int(a) + int(b))
