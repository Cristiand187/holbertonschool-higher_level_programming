#!/usr/bin/python3
"""Module"""
from sys import argv
from pathlib import Path
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file


def add_item(argument):
    """[summary]

    Arguments:
        argument {[type]} -- [description]
    """
    filename = 'add_item.json'

    if Path(filename).is_file():
        my_list = load_from_json_file(filename)
    else:
        my_list = []
    for elem in range(1, len(argv)):
        my_list.append(argv[elem])
    save_to_json_file(my_list, filename)


if __name__ == "__main__":
    add_item(argv)
