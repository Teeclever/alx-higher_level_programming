#!/usr/bin/python3

"""
Write a class Square that defines a square by: (based on 2-square.py
that returns the current square area
"""


class Square:
    """
    Declearing the variables self and size.

    """
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """
         a method that Calculates area of square
        Returns: area
        """
        return (self.__size ** 2)
