#!/usr/bin/python3
"""Module File"""


def read_lines(filename="", nb_lines=0):
    """[summary]

    Keyword Arguments:
        filename {str} -- [description] (default: {""})
        nb_lines {int} -- [description] (default: {0})
    """
    n_lines = 0
    with open(filename, encoding='utf-8') as file:
        for line in file:
            if nb_lines == n_lines and nb_lines > 0:
                break
            print(line, end="")
            n_lines += 1
    file.close()
