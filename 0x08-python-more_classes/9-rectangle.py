#!/usr/bin/python3
"""
    Define a Rectangle class with width and height.
"""


class Rectangle:
    """Representation of a Rectangle class"""

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Initialize a rectangle instance.

        Args:
            width (int, optional): width of the rectangle. Defaults to 0.
            height (int, optional): height of the rectangle. Defaults to 0.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """ Getter function for private variable, width """
        return self.__width

    @width.setter
    def width(self, value):
        """ Setter function for private variable, width.

        Args:
            value (int): The new width to set.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """ Getter function for private variable, height """
        return self.__height

    @height.setter
    def height(self, value):
        """Setter function for private variable, height.

        Args:
            value (int): The new height to set.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Computes and returns the area of the rectangle."""
        return self.height * self.width

    def perimeter(self):
        """Computes and returns the perimeter of the rectangle."""
        if any((self.height == 0, self.width == 0)):
            return 0
        return 2*(self.height + self.width)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Computes and returns the largest rectangle.

        Args:
            rect_1 (Rectangle): First rectangle object to be compared.
            rect_2 (Rectangle): Second rectangle object to be compared.

        Raises:
            TypeError: If either of the arguments is not instance of Rectangle.

        Returns:
            Rectangle: Largest rectangle, or rect_1 if they have same area.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        return rect_1 if rect_1.area() >= rect_2.area() else rect_2.area()

    @classmethod
    def square(cls, size=0):
        """Returns a new Rectangle instance."""
        return Rectangle(size, size)

    def __str__(self) -> str:
        """Draws the square.

        Returns:
            str: The square represented by given symbol.
        """
        if any((self.width == 0, self.height == 0)):
            return ""
        symbol = str(self.print_symbol)
        return "\n".join((symbol * self.width) for _ in range(self.height))

    def __repr__(self) -> str:
        """eval() compatible representation of object

        Returns:
            str: String representation of object that can be used with eval()
        """
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """Prints a message when an instance is deleted."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
