#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):

    try:
        elem = 0
        for item in range(x):
            print(my_list[item], end='')
            elem += 1
        print()
        return elem

    except (IndexError):
        print()
        return elem
