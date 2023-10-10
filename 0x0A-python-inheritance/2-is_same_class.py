#!/usr/bin/python3
"""Function"""


def is_same_class(obj, a_class) -> bool:
    """Checks if `obj` is an exact instance of `a_class`.

    Args:
        obj (any): Any data type
        a_class (ant): Any class object

    Returns:
        bool: True or False
    """
    return type(obj) is a_class
