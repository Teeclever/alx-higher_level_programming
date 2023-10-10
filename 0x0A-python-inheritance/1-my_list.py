#!/usr/bin/python3
"""Defines a class MyList."""


class MyList(list):
    """A custom class that inherits from `list`.
    Methods: print_sorted(self)
    """

    def __init__(self):
        """initializer for mylist"""

        super().__init__()

    def print_sorted(self):
        """Prints the list item in sorted order."""
        print(sorted(self))
