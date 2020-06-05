#!/usr/bin/python3
"""Module:"""


def append_after(filename="", search_string="", new_string=""):
    """[summary]

    Args:
        filename (str, optional): [description]. Defaults to "".
        search_string (str, optional): [description]. Defaults to "".
        new_string (str, optional): [description]. Defaults to "".
    """
    with open(filename, mode="r+", encoding="utf-8") as readFile:
        temp = readFile.readlines()

    count = 0
    with open(filename, mode="w", encoding="utf-8") as writeFile:
        for lines in temp:
            count += 1
            if search_string in lines:
                temp.insert(count, new_string)
        for lines in temp:
            writeFile.write(lines)
