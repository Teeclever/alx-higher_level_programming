#!/usr/bin/python3
"""Square Module"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Defines a Square class."""

    def __init__(self, size: int):
        super().integer_validator("size", size)
        self.__size = size

    def area(self) -> int:
        """Computes the area of the rectangle.

        Returns:
            int: The area.
        """
        return self.__size * self.__size

    def __str__(self):
        return f"[Rectangle] {self.__size}/{self.__size}"
