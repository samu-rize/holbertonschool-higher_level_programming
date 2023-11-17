#!/usr/bin/python3
"""Simple script to append text to a file."""


def append_write(filename="", text=""):
    """Appends the specified text to the given file."""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
