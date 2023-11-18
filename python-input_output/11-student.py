#!/usr/bin/python3
"""Defines a simple Student class and its to_json method."""


class Student:
    """Represents a student with first name, last name, and age."""

    def __init__(self, first_name, last_name, age):
        """Initializes a new Student instance."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Converts the Student instance to a JSON-serializable dictionary,
        optionally filtering attributes."""
        if attrs is None:
            return self.__dict__
        else:
            filter = {}
            for atr in attrs:
                if hasattr(self, atr):
                    filter[atr] = getattr(self, atr)
            return filter

    def reload_from_json(self, json):
        """Updates the Student instance from a JSON-serializable dictionary."""
        for key, val in json.items():
            setattr(self, key, val)
