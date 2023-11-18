#!/usr/bin/python3
"""Converts a class instance to a JSON-serializable dictionary."""


def class_to_json(obj):
    """Converts the specified class instance to a JSON-serializable
    dictionary."""
    return obj.__dict__
