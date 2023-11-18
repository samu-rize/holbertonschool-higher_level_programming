#!/usr/bin/python3
"""Simple script to save a Python object to a JSON file."""
import json


def save_to_json_file(my_obj, filename):
    """Writes the specified Python object to the given JSON file."""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
