#!/usr/bin/python3
"""From JSON String to Object"""
import json


def from_json_string(my_str):
    """Converts a JSON String to a Python data structure.

    Args:
        my_obj (str): String object to be converted

    Return:
        str: The Python object.
    """
    return json.loads(my_str)
