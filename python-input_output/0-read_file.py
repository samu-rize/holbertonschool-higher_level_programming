#!/usr/bin/python3
"""Simple script to read and print the contents of a file."""


def read_file(filename=""):
    """Reads and prints the contents of the specified file."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
