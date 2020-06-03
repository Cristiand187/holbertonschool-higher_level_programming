#!/usr/bin/python3
"""Module"""
import json


def load_from_json_file(filename):
    """[summary]

    Arguments:
        filename {[type]} -- [description]

    Returns:
        [type] -- [description]
    """
    str_json = ""
    with open(filename, encoding='utf-8') as file:
        for line in file:
            str_json += line
    return json.loads(str_json)
