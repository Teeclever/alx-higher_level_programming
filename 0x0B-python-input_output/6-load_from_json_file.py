#!/usr/bin/python3
"""Create object from a JSON file"""
import json


def load_from_json_file(filename):
    """creates an Object from a “JSON file”.

    Args:
        filename (str): JSON file to be read from.
    """
    with open(filename, mode="r", encoding="utf-8") as s:
        return json.load(s)
