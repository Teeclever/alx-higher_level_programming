#!/usr/bin/python3
"""Only sub class of"""


def inherits_from(obj, a_class):
    """
        Checks if `obj` is an instance of a subclass of `a_class`
        but not exactly an instance of `a_class` itself.

    Args:
        obj (any): Any data type
        a_class (ant): Any class object

    Returns:
        bool: True or False
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
