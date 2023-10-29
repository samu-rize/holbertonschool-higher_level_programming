#!/usr/bin/python3
"""Write a class Square that defines a square by size
    and calculate the current square area"""


class Square:
    """
    This is a simple Python class to represent a square.

    Attributes:
        __size (int): The size of the square.

    Methods:
        __init__(self, size=0): Constructor method to initialize the square with a given size.
        area(self): Calculate the area of the square.
    """
    def __init__(self, size=0):
        """
        Initializes a new Square instance with the specified size.

        Args:
            size (int): The size of the square.

        Returns:
            None

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is a negative integer.
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        """
        Calculate the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square.

        Args:
            value (int): The new size of the square.

        Returns:
            None

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is a negative integer.
        """
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value