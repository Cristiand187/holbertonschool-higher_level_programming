#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):

    try:
        for idx, elem in enumerate(my_list):
            if idx < x:
                print(elem, end='')
            else:
                break
        print()

        return idx + 1 if idx < x else x

    except Exception as inst:
        print(type(inst))
