#!/usr/bin/python3
"""Add-Attribute Module"""


def add_attribute(obj, name, value):
    """Tries to add an attribute to an object.

    Args:
        obj (object): The object we want to add an attribute to.
        name (str): The name of the attribute to be added.
        value (any): The value of the attribute to be added.

    Raises:
        TypeError: If the object does not have a dict attribute,
                   meaning a new attribute can't be added.
    """
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")

    setattr(obj, name, value)
