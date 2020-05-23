#!/usr/bin/python3
"""[summary]    """


def print_square(size):
    """[summary]

    Arguments:
        size {[type]} -- [description]

    Raises:
        ValueError: [description]
        ValueError: [description]
    """

    if (type(size) != int):
        raise TypeError("size must be an integer")
    elif (size < 0):
        raise ValueError("size must be >= 0")
    else:
        n = 1 if size == 0 else size

        for i in range(size):
            for j in range(size):
                print('' if size == 0 else '#', end='')
            print()
