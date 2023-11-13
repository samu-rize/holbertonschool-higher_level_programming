#!/usr/bin/python3
def add_integer(a, b=98):
    if not (isinstance(a, int) or isinstance(a, float)):
        raise TypeError("{} must be an integer".format(a))
    elif not (isinstance(b, int) or isinstance(b, float)):
        raise TypeError("{} must be an integer".format(b))
    return int(a) + int(b)
