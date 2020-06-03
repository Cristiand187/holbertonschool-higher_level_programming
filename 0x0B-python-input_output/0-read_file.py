#!/usr/bin/python3
"""module file"""


def read_file(filename=""):
    """[summary]

    Keyword Arguments:
        filename {str} -- [description] (default: {""})
    """
    with open(filename, encoding='utf-8') as file:
        for line in file:
            print(line, end="")
    file.close()
