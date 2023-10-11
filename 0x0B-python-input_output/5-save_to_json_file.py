#!/usr/bin/python3
"""Save Object to a file"""
import json


def save_to_json_file(my_obj, filename):
    """Writes an Object to a text file, using a JSON representation.

    Args:
        my_obj (any): Object to be written.
        filename (str): File to be written to.
    """
    with open(filename, mode="w", encoding="utf-8") as s:
        json.dump(my_obj, s)
