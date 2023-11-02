#!/usr/bin/python3
"""Defines a class Square that represents a square by size and calculates
its area."""


class Square:
    """Initializes a Square instance with the specified size and position."""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes a new Square instance with the specified size and
        position."""
        self.__size = size
        self.__position = position

    def area(self):
        """Calculates the area of the square."""
        return self.__size ** 2

    @property
    def size(self):
        """Get the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square."""
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    @property
    def position(self):
        """Get the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the position of the square."""
        if (not isinstance(value, tuple) or
                (len(value) is not 2) or
                not all(isinstance(num, int) for num in value) or
                all(num < 0 for num in value)):
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    def my_print(self):
        """Prints the square with '#' characters."""
        if self.__size == 0:
            print()
        else:
            print('{}'.format('\n' * self.__position[1]), end='')
            for _ in range(self.__size):
                print(
                    '{}{}'.format(
                        '_' * self.__position[0],
                        '#' * self.__size))
