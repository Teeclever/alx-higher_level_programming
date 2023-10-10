#!/usr/bin/python3

"""A function that returns True if the object is exactly an instance of t
he specified class
"""


def is_same_class(obj, a_class):
    """
    Function that checks if the object
    is exactly an instance of a_class
    Args:
    obj: object
    a_class: class

    """
    if type(obj) == a_class:
        return True
    else:
        return False
