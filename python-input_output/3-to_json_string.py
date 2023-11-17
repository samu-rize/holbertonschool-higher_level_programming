#!/usr/bin/python3
"""Simple script to convert a Python object to a JSON string."""
import json


def to_json_string(my_obj):
    """Converts the specified Python object to a JSON-formatted string."""
    return json.dumps(my_obj)
