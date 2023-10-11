#!/usr/bin/python3
"""Reads and prints the contents of a text file."""


def read_file(filename=""):
    """Reads a text file and prints it to stdout.

    Args:
        filename (str, optional): Path to the text file. Defaults to "".
    """
    with open(filename, mode="r", encoding="utf-8") as s:
        print(s.read(), end="")
