#!/usr/bin/python3
def find_peak(list_of_integers):
    """ Python function to find peak number"""

    if len(list_of_integers) > 0:
        list_ = list_of_integers.sort()
        return list_[-1]
    else:
        return None
