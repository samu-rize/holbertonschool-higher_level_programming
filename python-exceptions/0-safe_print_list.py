#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):

    idx = 0

    for idx in range(x):
        try:
            print(my_list[idx], end='')
        except IndexError:
            print()
            return idx

    print()
    return idx + 1
