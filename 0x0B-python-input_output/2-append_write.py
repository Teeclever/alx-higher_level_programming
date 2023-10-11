#!/usr/bin/python3
"""Append-File"""


def append_write(filename="", text=""):
    """Appends a string to a text file.

    Args:
        filename (str, optional): Path to the text file. Defaults to "".
        text (str, optional): Text to be appended. Defaults to "".
    """
    with open(filename, mode="a", encoding="utf-8") as s:
        return s.write(text)
