#!/usr/bin/python3
"""[summary]"""


def say_my_name(first_name, last_name=""):
    """[summary]

    Arguments:
        first_name {[type]} -- [description]

    Keyword Arguments:
        last_name {str} -- [description] (default: {""})

    Raises:
        TypeError: [description]
        TypeError: [description]
    """
    if type(first_name) not in [str]:
        raise TypeError("first_name must be a string")
    elif type(last_name) not in [str]:
        raise TypeError("last_name must be a string")
    else:
        print("My name is {} {}".format(first_name, last_name))
