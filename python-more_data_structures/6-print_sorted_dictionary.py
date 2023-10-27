#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    if a_dictionary is not None:
        sorted_dict = dict(sorted(a_dictionary.items()))

        for key, val in sorted_dict.items():
            print('{}: {}'.format(key, val))
