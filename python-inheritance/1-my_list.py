#!/usr/bin/python3
"""This is a simple script with a MyList class."""


class MyList(list):
    """MyList is a subclass of the built-in list class."""
    def print_sorted(self):
        """This method prints the sorted elements of the list."""
        copy = sorted(self)
        print(copy)
