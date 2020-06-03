#!/usr/bin/python3
"""module file"""


def number_of_lines(filename=""):
    """[summary]

    Keyword Arguments:
        filename {str} -- [description] (default: {""})

    Returns:
        [type] -- [description]
    """
    n_line = 0
    with open(filename, encoding='utf-8') as file:
        for line in file:
            n_line += 1
    return n_line
