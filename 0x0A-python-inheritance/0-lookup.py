#!/usr/bin/python3
"""Lookup Function"""


def lookup(obj) -> list:
    """Returns the list of available attributes and methods of an object.

    Args:
        obj: The object to be scanned.

    Returns:
        list: A list of the objects attributes and methods.
    """
    return dir(obj)
