#!/usr/bin/python3

"""
A class Square that defines a square by

Private instance attribute

"""


class Square:
    """
    delearing the variables self and size.
    to declear

    """
    def __init__(self, size=0):

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
