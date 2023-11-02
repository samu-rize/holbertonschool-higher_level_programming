#!/usr/bin/python3
"""Write a class Square that defines a square by size
    and calculate the current square area"""


class Square:
    """
    This is a simple Python class to represent a square.

    Attributes:
        __size (int): The size of the square.

    Methods:
        __init__(self, size=0): Constructor method to initialize the square
        with a given size.
        area(self): Calculate the area of the square.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a new Square instance with the specified size and position.

        Args:
            size (int): The size of the square.
            position (tuple of int): The position of the square.

        Returns:
            None

        Raises:
            TypeError: If size is not an integer or if position is not a tuple
                of 2 integers.
            ValueError: If size or position contains negative values.
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
        self.__position = position

    def area(self):
        """
        Calculate the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    @property
    def size(self):
        """
        Get the size of the square.

        Returns:
            int: The size of the square.
        """
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

    @property
    def position(self):
        """
        Get the position of the square.

        Returns:
            tuple of int: The position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Set the position of the square.

        Args:
            value (tuple of int): The new position of the square.

        Returns:
            None

        Raises:
            TypeError: If value is not a tuple of 2 integers.
            ValueError: If value contains negative values.
        """
        if (not isinstance(value, tuple) or
            (len(value) is not 2) or
            not all(isinstance(num, int) for num in value) or
                all(num < 0 for num in value)):
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    def my_print(self):
        """
        Print the square with '#' characters.

        Returns:
            None
        """
        if self.__size == 0:
            print()
        else:
            print('{}'.format('\n' * self.__position[1]), end='')
            for _ in range(self.__size):
                print(
                    '{}{}'.format(
                        ' ' * self.__position[0],
                        '#' * self.__size))
