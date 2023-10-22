#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if not my_list:
        return
    new = my_list.copy()
    if (idx < 0) or (idx not in range(len(my_list))):
        return new
    new[idx] = element
    return new
