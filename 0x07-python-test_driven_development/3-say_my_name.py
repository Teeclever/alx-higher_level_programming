#!/usr/bin/python3
"""This module contains a function that prints a person's full name."""


def say_my_name(first_name, last_name=""):
    """Prints a person's full name.

    Args:
        first_name (str): First name
        last_name (str, optional): Last name. Defaults to "".

    Raises:
        TypeError: If first name is not a string.
        TypeError: If last name is not a string.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
