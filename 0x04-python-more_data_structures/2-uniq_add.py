#!/usr/bin/python3
def uniq_add(my_list=[]):
    list_set = set(my_list)
    sum = 0
    unique_list = (list(list_set))
    for num in unique_list:
        sum += num
    return (sum)
