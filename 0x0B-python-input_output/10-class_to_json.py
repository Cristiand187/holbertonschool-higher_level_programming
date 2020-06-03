#!/usr/bin/python3
"""module json"""


def class_to_json(obj):
    """[summary]

    Arguments:
        obj {[type]} -- [description]

    Returns:
        [type] -- [description]
    """
    return obj.__dict__
