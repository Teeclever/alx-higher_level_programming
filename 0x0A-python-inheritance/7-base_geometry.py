#!/usr/bin/python3
"""Geometry module"""


class BaseGeometry:
    """Defines a BaseGeometry class."""

    def area(self):
        """Computes the area of the geometry.

        Raises:
            Exception: Because the logic is not implemented yet.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name: str, value: int):
        """Validates `value`.

        Args:
            name (str): Name
            value (int): Value

        Raises:
            TypeError: If `value` is not an integer.
            ValueError: If `value` is not a positive, non-zero integer.
        """
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError(f"{name} must be an integer")

        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
