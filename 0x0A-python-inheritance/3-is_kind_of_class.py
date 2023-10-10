#!/usr/bin/python3
"""
Creates a function that returns true
if prototype is_kind_of_class(obj)
"""


def is_kind_of_class(obj, a_class):
    """A function that check is an obkect is an instance a class
    or that of the inherited from
    args:
    obj: the object to be checked
    a_class: the class
    Return:Ture if valid or false when wrong
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
