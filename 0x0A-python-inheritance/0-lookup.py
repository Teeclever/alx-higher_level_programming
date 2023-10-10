#!/usr/bin/python3

"""
Creates a function with the prototype lookup(obj).
"""


def lookup(obj):
    """
    Funcion that returns list of available attributes
    """
    return dir(obj)
