#!/usr/bin/python3
"""Same Class or Inherited From"""


def is_kind_of_class(obj, a_class):
    """Checks if `obj` is an instance of `a_class` or `object`.

    Args:
        obj (any): Any data type
        a_class (ant): Any class object

    Returns:
        bool: True or False
    """
    return isinstance(obj, a_class)
