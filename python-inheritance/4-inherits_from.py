#!/usr/bin/python3
"""Inheritance check."""


def inherits_from(obj, a_class):
    """Check if obj inherits from a_class."""
    return type(obj) is not a_class and issubclass(type(obj), a_class)
