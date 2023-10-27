#!/usr/bin/python3
def search_replace(my_list, search, replace):
    newlist = []
    for idx in my_list:
        if idx == search:
            newlist.append(replace)
        else:
            newlist.append(idx)
    return newlist
