#!/usr/bin/python3
"""Module for Square class"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Constructor"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Overrides the __str__ method"""
        return "[{}] ({}) {}/{} - {}".format(type(self).__name__,
                                             self.id, self.x, self.y,
                                             self.width)

    @property
    def size(self):
        """Getter"""
        return self.width

    @size.setter
    def size(self, value):
        """setter"""
        self.width = value
        self.height = value

    def __update(self, id=None, size=None, x=None, y=None):
        """Updates attributes based on input parameters"""
        if id is not None:
            self.id = id
        if size is not None:
            self.size = size
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def update(self, *args, **kwargs):
        """assigns arguments to each attribute"""
        if not kwargs:
            self.__update(*args)
        else:
            self.__update(*args, **kwargs)

    def to_dictionary(self):
        """dictionary representation"""
        return {"id": self.id, "size": self.width,
                "x": self.x, "y": self.y}
