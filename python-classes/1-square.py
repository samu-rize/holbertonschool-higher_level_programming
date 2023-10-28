#!/usr/bin/python3
"""Square module"""


class Square:
    """
    This is a simple Python class to represent a square.

    Attributes:
        __size (int): The size of the square.

    Methods:
        __init__(self, size): Constructor method to initialize the square with
        a given size.
    """
    def __init__(self, size):
        """
        Initializes a new Square instance with the specified size.

        Args:
            size (int): The size of the square.

        Returns:
            None
        """
        self.__size = size
