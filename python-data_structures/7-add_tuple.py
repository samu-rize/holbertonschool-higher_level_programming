#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tup_a = [0, 0]
    tup_b = [0, 0]

    for i in range(2):
        if i < len(tuple_a):
            tup_a[i] = tuple_a[i]
        if i < len(tuple_b):
            tup_b[i] = tuple_b[i]
    for i in range(2):
        tup_a[i] += tup_b[i]
    final_tuple = tup_a[0], tup_a[1]
    return final_tuple
