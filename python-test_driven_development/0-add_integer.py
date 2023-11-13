#!/usr/bin/python3
"""module contain a functions to add 2 integers"""


def add_integer(a, b=98):
    """function add 2 integers"""
    if not (isinstance(a, int) or isinstance(a, float)):
        raise TypeError("{} must be an integer".format(a))
    elif not (isinstance(b, int) or isinstance(b, float)):
        raise TypeError("{} must be an integer".format(b))
    return int(a) + int(b)

    if __name__ == "__main__":
        import doctest
        doctest.testfile("tests/0-add_integer.txt")
