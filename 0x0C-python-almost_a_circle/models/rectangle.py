#!/usr/bin/python3
"""
    Rectangle Module
"""
from models.base import Base


class Rectangle(Base):
    """Defines a Rectangle class."""
    def __init__(self, width: int, height: int, x=0, y=0, id=None):
        """
        Initializes a Rectangle object.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int, optional): The x-coordinate of the rectangle's position.
                            Defaults to 0.
            y (int, optional): The y-coordinate of the rectangle's position.
                            Defaults to 0.
            id (optional): The identifier of the rectangle. Defaults to None.
        """
        super().__init__(id)
        self._validate_attr(width, "width")
        self._validate_attr(height, "height")
        self._validate_attr(x, "x")
        self._validate_attr(y, "y")
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    # >>>>>>>>>>>>>>>>>>>   WIDTH   <<<<<<<<<<<<<<<<<<<<
    @property
    def width(self) -> int:
        """
        int: The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value: int):
        """
        Sets the width of the rectangle.

        Args:
            value (int): The new width value.
        """
        self._validate_attr(value, "width")
        self.__width = value

    # >>>>>>>>>>>>>>>>>>>   HEIGHT   <<<<<<<<<<<<<<<<<<<<
    @property
    def height(self) -> int:
        """
        int: The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value: int):
        """
        Sets the height of the rectangle.

        Args:
            value (int): The new height value.
        """
        self._validate_attr(value, "height")
        self.__height = value

    # >>>>>>>>>>>>>>>>>>>   X   <<<<<<<<<<<<<<<<<<<<
    @property
    def x(self) -> int:
        """
        int: The x-coordinate of the rectangle's position.
        """
        return self.__x

    @x.setter
    def x(self, value: int):
        """
        Sets the x-coordinate of the rectangle's position.

        Args:
            value (int): The new x-coordinate value.
        """
        self._validate_attr(value, "x")
        self.__x = value

    # >>>>>>>>>>>>>>>>>>>   Y   <<<<<<<<<<<<<<<<<<<<
    @property
    def y(self) -> int:
        """
        int: The y-coordinate of the rectangle's position.
        """
        return self.__y

    @y.setter
    def y(self, value: int):
        """
        Sets the y-coordinate of the rectangle's position.

        Args:
            value (int): The new y-coordinate value.
        """
        self._validate_attr(value, "y")
        self.__y = value

    def _validate_attr(self, value: int, name: str):
        """
        Validates the attribute value.

        Args:
            value (int): The attribute value to validate.
            name (str): The name of the attribute.
        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is invalid for width,
                        height, x, or y attributes.
        """
        if not isinstance(value, int):
            err_msg = f"{name} must be an integer"
            raise TypeError(err_msg)

        if name in {"width", "height"} and value <= 0:
            err_msg = f"{name} must be > 0"
            raise ValueError(err_msg)

        if name in {"x", "y"} and value < 0:
            err_msg = f"{name} must be >= 0"
            raise ValueError(err_msg)

    def area(self) -> int:
        """
        Calculates the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.__height * self.__width

    def display(self):
        """
        Displays the rectangle on the console.
        """
        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            print((" " * self.__x) + ("#" * self.__width))

    def to_dictionary(self) -> dict:
        """
        Converts the rectangle to a dictionary representation.

        Returns:
            dict: A dictionary representing the rectangle.
        """
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }

    def update(self, *args, **kwargs):
        """
        Updates the rectangle's attributes.

        Args:
            *args: The positional arguments can be used to update id,
                   width, height, x, and y in that order.
            **kwargs: The keyword arguments can be used to update any
                   attribute by specifying the attribute name.
        """
        try:
            if args:
                attrs = ("id", "width", "height", "x", "y")
                for idx, arg in enumerate(args):
                    setattr(self, attrs[idx], arg)
            else:
                for key, value in kwargs.items():
                    setattr(self, key.lower(), value)
        except (IndexError, AttributeError):
            return

    def __str__(self) -> str:
        """
        Returns a string representation of the rectangle.

        Returns:
            str: The string representation of the rectangle.
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height
        )
