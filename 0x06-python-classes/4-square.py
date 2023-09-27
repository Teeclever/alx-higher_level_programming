#!/usr/bin/python3

"""
A class Square that defines a square by private instance attribute: size
with also a  public instance method
"""


class Square:
    """
    Declearing the variables self and size.
    """
    def __init__(self, size=0):

        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        # Update the private instance attribute
        self.__size = value

    def area(self):
        """
        A method that Calculates area of square

        """
        return (self.__size ** 2)
