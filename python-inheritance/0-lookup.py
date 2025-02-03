#!/usr/bin/python3
"""Module that defines the lookup function."""


def lookup(obj):
    """
    Return a list of available attributes and methods of an object.

    Ar
        obj: The object whose attributes and methods are to be returned.

    Returns:
        list: A list of strings representing the attributes and methods
        of th object.
    ""
    return dir(obj)
