#!/usr/bin/python3
"""
class MyList that inherits from list
"""


class MyList(list):
    """[summary]

    Arguments:
        list {[type]} -- [description]
    """
    def print_sorted(self):
        """[summary]
        """
        new_list = self.copy()
        new_list.sort()
        print(new_list)
