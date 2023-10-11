#!/usr/bin/python3
"""Write-File"""


def write_file(filename="", text=""):
    """Writes a string to a text file.

    Args:
        filename (str, optional): Path to the text file. Defaults to "".
        text (str, optional): Text to be written. Defaults to "".
    """
    with open(filename, mode="w", encoding="utf-8") as s:
        return s.write(text)
