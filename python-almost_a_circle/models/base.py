#!/usr/bin/python3
"""Defines a simple Base class for managing unique IDs."""

from json import dumps, loads


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
        return dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """JSON string to file"""
        if list_objs is not None:
            list_objs = [obj.to_dictionary() for obj in list_objs]
        with open("{}.json".format(cls.__name__), "w", encoding="utf-8") as f:
            f.write(cls.to_json_string(list_objs))

    @staticmethod
    def from_json_string(json_string):
        """JSON string to dictionary"""
        if json_string is None or not json_string:
            return []
        return loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Dictionary to Instance"""
        from models.rectangle import Rectangle
        from models.square import Square
        if cls is Rectangle:
            dummy = Rectangle(1, 1)
        elif cls is Square:
            dummy = Square(1)
        else:
            dummy = None
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """load string from file"""
        from os import path
        file = "{}.json".format(cls.__name__)
        if not path.isfile(file):
            return []
        with open(file, "r", encoding="itf-8") as f:
            return [cls.create(**d) for d in cls.from_json_string(f.read())]
