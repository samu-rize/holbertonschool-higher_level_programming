#!/usr/bin/python3
"""Rectangle module"""


class Rectangle:
    """Simple Python class to represent a Rectangle."""

    # Created public class attribute number_of_instances
    # Initialized to 0
    number_of_instances = 0  

    def __init__(self, width=0, height=0):
        """Initialize a Rectangle with optional width and height."""

        self.width = width
        self.height = height
        # Incremented during each new instance instantiation
        Rectangle.number_of_instances += 1


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

    def __repr__(self):
        """Return a string representation of the Rectangle for developers."""
        return ("Rectangle({}, {})".format(self.width, self.height))

    def __del__(self):
        """Destructor method to perform cleanup when the object is deleted."""
        del self
        print("Bye rectangle...")
        # Decremented during each instance deletion
        Rectangle.number_of_instances -= 1
