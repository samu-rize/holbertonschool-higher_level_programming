#!/usr/bin/python3
"""Defines a simple Student class and its to_json method."""


class Student:
    """Represents a student with first name, last name, and age."""

    def __init__(self, first_name, last_name, age):
        """Initializes a new Student instance."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Converts the Student instance to a JSON-serializable dictionary."""
        return self.__dict__
