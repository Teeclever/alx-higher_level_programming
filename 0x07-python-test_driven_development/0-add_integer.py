#!/usr/bin/python3
""" A module contains a simple function that returns the sum of integer
"""


def add_integer(a, b=98) -> int:
    """ compute and returns the sum of 2 integers.

    Args:
        a (int or float): First number to be added.
        b (int or float): Second number to be added.

    Raises:
        TypeError: If either of the arguments is not an integer or float.

    Returns:
        int: Sum of the 2 numbers.
    """
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return a + b
