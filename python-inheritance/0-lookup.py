#!/usr/bin/python3
"""Define an object attr lookup function"""


def lookup(obj):
    """return a list of the obj's attributes"""
    return dir(obj)
