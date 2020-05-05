#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    cp_list = my_list.copy()
    if (idx < 0):
        return(cp_list)
    elif (len(cp_list)-1 < idx):
        return (cp_list)
    elif (cp_list[idx] <= 0):
        return (cp_list)
    else:
        cp_list[idx] = element
        return (cp_list)
