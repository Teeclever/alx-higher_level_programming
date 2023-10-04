#!/usr/bin/python3
"""This module contains a function that splits text by specified delimiters."""


def text_indentation(text):
    """Prints text separated by deliiters, line by line.

    Args:
        text (str): Text to print.

    Raises:
        TypeError: If text given is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    if not text:
        return

    chars = ""
    splited = []
    for char in text:
        chars += char
        if char in ".?:":
            splited.append(chars.strip())
            chars = ""

    if chars:
        splited.append("".join(chars).strip())

    for line in splited[:-1]:
        print(line)
        print("")
    print(splited[-1], end="")
