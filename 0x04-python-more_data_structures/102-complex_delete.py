#!/usr/bin/python3
def complex_delete(my_dict, value):
    dele = []
    for key in my_dict:
        if my_dict[key] == value:
            dele.append(key)
    for key in dele:
        del my_dict[key]
    return my_dict
