#!/usr/bin/python3
"""
    Square Module
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Defines a Square class."""

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes a new Square object.

        Args:
            size (int): The length of one side of the square.
            x (int, optional): The x-coordinate of the top-left
                               corner of the square. Defaults to 0.
            y (int, optional): The y-coordinate of the top-left
                               corner of the square. Defaults to 0.
            id (str, optional): A unique identifier for the square.
                               Defaults to None.
        """
        self._validate_attr(size, "width")
        self._validate_attr(x, "x")
        self._validate_attr(y, "y")
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        Returns the length of one side of the square.

        Returns:
            int: The length of one side of the square.
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Sets the length of one side of the square.

        Args:
            value (int): The length of one side of the square.
        """
        self._validate_attr(value, "width")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Updates the attributes of the square.

        Args:
            *args: A list of attributes to update.
            **kwargs: A dictionary of attributes to update.
        """
        try:
            if args:
                attrs = ["id", "size", "x", "y"]
                for x, arg in enumerate(args):
                    setattr(self, attrs[x], arg)
            else:
                for key, value in kwargs.items():
                    setattr(self, key, value)
        except (IndexError, AttributeError):
            return

    def to_dictionary(self):
        """
        Returns a dictionary representation of the square.

        Returns:
            dict: A dictionary with the square's attributes.
        """
        return {"id": self.id, "size": self.width, "x": self.x, "y": self.y}

    def __str__(self):
        """
        Returns a string representation of the square.

        Returns:
            str: A string with the square's attributes.
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
