#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dict = a_dictionary.copy()
    for key, val in new_dict.items():
        new_dict.update({key: val * 2})
    return new_dict
