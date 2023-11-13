#!/usr/bin/python3
"""class Square that inherits from Rectangle"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """class Square"""
    def __init__(self, size):
        """create new square"""
        size.integer_validator("size", size)
        self.__size = size
