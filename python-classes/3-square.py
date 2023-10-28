#!/usr/bin/python3
"""Square module"""


class Square:

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
        return self.__size * self.__size
