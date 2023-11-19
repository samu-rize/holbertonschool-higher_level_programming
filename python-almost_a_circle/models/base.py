#!/usr/bin/python3
"""Defines a simple Base class for managing unique IDs."""


class Base:
    """Represents a base class with a unique ID generator."""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes a new instance with a unique ID."""
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
