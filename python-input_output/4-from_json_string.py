#!/usr/bin/python3
"""Simple script to convert a JSON string to a Python object."""
import json


def from_json_string(my_str):
    """Parses the specified JSON string and returns the corresponding Python object."""
    return json.loads(my_str)
