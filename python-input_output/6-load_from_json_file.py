#!/usr/bin/python3
"""Simple script to load a Python object from a JSON file."""
import json


def load_from_json_file(filename):
    """Reads a JSON file and returns the corresponding Python object."""
    with open(filename, "r") as jf:
        return json.load(jf)
