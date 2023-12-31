#!/usr/bin/python3
"""Rectangle module"""


class Rectangle:
    """Simple Python class to represent a Rectangle."""

    def __init__(self, width=0, height=0):
        """Initialize a Rectangle with optional width and height."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the Rectangle."""
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """Get the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the Rectangle."""
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """Calculate and return the area of the Rectangle."""
        return self.__width * self.height

    def perimeter(self):
        """Calculate and return the perimeter of the Rectangle."""
        if not self.__width or not self.__height:
            return 0
        return (self.width + self.height) * 2

    def __str__(self) -> str:
        """Return a string representation of the Rectangle for printing."""
        if not self.width or not self.height:
            return ""
        return "\n".join(["#" * self.__width] * self.height)
