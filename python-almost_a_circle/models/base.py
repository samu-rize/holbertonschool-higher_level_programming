#!/usr/bin/python3
"""Defines a simple Base class for managing unique IDs."""

from json import dumps


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """Dictionary to JSON string"""
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        else:
            return dumps(list_dictionaries)
