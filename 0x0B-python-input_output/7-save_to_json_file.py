#!/usr/bin/python3
"""module"""
import json


def save_to_json_file(my_obj, filename):
    """[summary]

    Arguments:
        my_obj {[type]} -- [description]
        filename {[type]} -- [description]
    """
    with open(filename, mode='w', encoding='utf-8') as file:
        file.write(json.dumps(my_obj))
    file.close()
