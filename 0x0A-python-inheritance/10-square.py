#!/usr/bin/python3
"""Square Module"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Defines a Square class."""

    def __init__(self, size):
        """initalizer
        Args
           size: size of side of square
        """
        super().integer_validator("size", size)
        Rectangle.__init__(self, size, size)
