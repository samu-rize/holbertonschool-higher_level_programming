#!/usr/bin/python3
"""class Square that inherits from Rectangle"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """class Square"""
    def __init__(self, size):
        """create new square"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
            """return discription"""
            return "[Square] {}/{}".format(self.__size, self.__size)
