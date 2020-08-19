#!/usr/bin/python3
def find_peak(list_of_integers):
    """ Python function to find peak number"""
    return sorted(list_of_integers)[-1] if len(list_of_integers) > 0 else None
