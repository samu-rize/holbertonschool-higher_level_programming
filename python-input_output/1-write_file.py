#!/usr/bin/python3
"""Simple script to write text to a file."""


def write_file(filename="", text=""):
    """Writes the specified text to the given file."""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
