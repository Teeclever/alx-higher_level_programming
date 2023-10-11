#!/usr/bin/python3
"""Class-to-JSON Function"""


def class_to_json(obj) -> dict:
    """Returns the dictionary representation of a simple data structure.

    Args:
        obj (object): An instance of a class.

    Return:
        dict: Dictionary representation of obj.
    """
    return obj.__dict__
