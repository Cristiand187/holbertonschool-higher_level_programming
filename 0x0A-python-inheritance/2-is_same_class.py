#!/usr/bin/python3
"""[summary]"""


def is_same_class(obj, a_class):
    """[summary]

    Arguments:
        obj {[type]} -- [description]
        a_class {[type]} -- [description]

    Returns:
        [type] -- [description]
    """
    if type(obj) is a_class:
        return True
    return False
