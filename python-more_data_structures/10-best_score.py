#!/usr/bin/python3
def best_score(a_dictionary):

    if a_dictionary is None:
        return None

    best_val = None
    best_key = ''

    for key, val in a_dictionary.items():
        if best_val is None or val > best_val:
            best_val = val
            best_key = key
    return best_key
