#!/usr/bin/python3

import io
import sys
import unittest
from pathlib import Path

from models.base import Base
from models.rectangle import Rectangle


class TestRectangleInstantiation(unittest.TestCase):
    """Unit tests for testing instantiation of the Rectangle class."""

    def setUp(self):
        self.rect = Rectangle(5, 7, 7, 5, 1)

    def test_inherits_base(self):
        """Test if Rectangle instance is an instance of Base."""
        self.assertIsInstance(Rectangle(10, 2), Base)

    def test_no_args(self):
        """Test if TypeError is raised when no arguments are provided."""
        with self.assertRaises(TypeError):
            Rectangle()

    def test_one_arg(self):
        """Test if TypeError is raised when only one argument is provided."""
        with self.assertRaises(TypeError):
            Rectangle(1)

    def test_two_args(self):
        """
        Test if ids of two Rectangles initialized with two arguments
        differ by 1.
        """
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        self.assertEqual(r1.id, r2.id - 1)

    def test_three_args(self):
        """
        Test if ids of two Rectangles initialized with three arguments
        differ by 1.
        """
        r1 = Rectangle(2, 2, 4)
        r2 = Rectangle(4, 4, 2)
        self.assertEqual(r1.id, r2.id - 1)

    def test_four_args(self):
        """
        Test if ids of two Rectangles initialized with four arguments
        differ by 1.
        """
        r1 = Rectangle(1, 2, 3, 4)
        r2 = Rectangle(4, 3, 2, 1)
        self.assertEqual(r1.id, r2.id - 1)

    def test_five_args(self):
        """
        Test if the id of a Rectangle initialized with five arguments
        is correct.
        """
        self.assertEqual(7, Rectangle(10, 2, 0, 0, 7).id)

    def test_over_five_args(self):
        """
        Test if TypeError is raised when more than five arguments
        are provided.
        """
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, 4, 5, 6)

    def test_private_width_attribute(self):
        """
        Test if AttributeError is raised when accessing the private
        width attribute.
        """
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__width)

    def test_private_height_attribute(self):
        """
        Test if AttributeError is raised when accessing the private height
        attribute.
        """
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__height)

    def test_private_x_attribute(self):
        """
        Test if AttributeError is raised when accessing the private x
        attribute.
        """
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__x)

    def test_private_y_attribute(self):
        """
        Test if AttributeError is raised when accessing the private y
        attribute.
        """
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__y)

    def test_width_getter(self):
        """Test if the width getter returns the correct value."""
        self.assertEqual(5, self.rect.width)

    def test_width_setter(self):
        """Test if the width setter updates the width attribute correctly."""
        self.rect.width = 10
        self.assertEqual(10, self.rect.width)

    def test_height_getter(self):
        """Test if the height getter returns the correct value."""
        self.assertEqual(7, self.rect.height)

    def test_height_setter(self):
        """Test if the height setter updates the height attribute correctly."""
        self.rect.height = 10
        self.assertEqual(10, self.rect.height)

    def test_x_getter(self):
        """Test if the x getter returns the correct value."""
        self.assertEqual(7, self.rect.x)

    def test_x_setter(self):
        """Test if the x setter updates the x attribute correctly."""
        self.rect.x = 10
        self.assertEqual(10, self.rect.x)

    def test_y_getter(self):
        """Test if the y getter returns the correct value."""
        self.assertEqual(5, self.rect.y)

    def test_y_setter(self):
        """Test if the y setter updates the y attribute correctly."""
        self.rect.y = 10
        self.assertEqual(10, self.rect.y)


class TestRectangleWidth(unittest.TestCase):
    """Unittests for testing initialization of Rectangle width attribute."""

    def test_none_width(self):
        """..."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(None, 2)

    def test_str_width(self):
        """..."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("invalid", 2)

    def test_float_width(self):
        """..."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(5.5, 1)

    def test_complex_width(self):
        """..."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(complex(5), 2)

    def test_dict_width(self):
        """..."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({"a": 1, "b": 2}, 2)

    def test_list_width(self):
        """..."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle([1, 2, 3], 2)

    def test_set_width(self):
        """..."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({1, 2, 3}, 2)

    def test_tuple_width(self):
        """..."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle((1, 2, 3), 2)

    def test_frozenset_width(self):
        """..."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(frozenset({1, 2, 3}), 2)

    def test_range_width(self):
        """..."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(range(5), 2)

    def test_bytes_width(self):
        """..."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(b"Python", 2)

    def test_bytearray_width(self):
        """..."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(bytearray(b"abcdefg"), 2)

    def test_memoryview_width(self):
        """..."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(memoryview(b"abcedfg"), 2)

    def test_inf_width(self):
        """..."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(float("inf"), 2)

    def test_nan_width(self):
        """..."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(float("nan"), 2)

    def test_negative_width(self):
        """..."""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-1, 2)

    def test_zero_width(self):
        """..."""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 2)


class TestRectangleHeight(unittest.TestCase):
    """Unittests for testing initialization of Rectangle height attribute."""

    def test_none_height(self):
        """..."""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, None)

    def test_str_height(self):
        """..."""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, "invalid")

    def test_float_height(self):
        """..."""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, 5.5)

    def test_complex_height(self):
        """..."""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, complex(5))

    def test_dict_height(self):
        """..."""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, {"a": 1, "b": 2})

    def test_list_height(self):
        """..."""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, [1, 2, 3])

    def test_set_height(self):
        """..."""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, {1, 2, 3})

    def test_tuple_height(self):
        """..."""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, (1, 2, 3))

    def test_frozenset_height(self):
        """..."""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, frozenset({1, 2, 3}))

    def test_range_height(self):
        """..."""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, range(5))

    def test_bytes_height(self):
        """..."""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, b"Python")

    def test_bytearray_height(self):
        """..."""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, bytearray(b"abcdefg"))

    def test_memoryview_height(self):
        """..."""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, memoryview(b"abcedfg"))

    def test_inf_height(self):
        """..."""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, float("inf"))

    def test_nan_height(self):
        """..."""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, float("nan"))

    def test_negative_height(self):
        """..."""
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(1, -1)

    def test_zero_height(self):
        """..."""
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(1, 0)


class TestRectangleX(unittest.TestCase):
    """Unittests for testing initialization of Rectangle x attribute."""

    def test_none_x(self):
        """..."""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, None)

    def test_str_x(self):
        """..."""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, "invalid", 2)

    def test_float_x(self):
        """..."""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, 5.5, 9)

    def test_complex_x(self):
        """..."""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, complex(5))

    def test_dict_x(self):
        """..."""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, {"a": 1, "b": 2}, 2)

    def test_list_x(self):
        """..."""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, [1, 2, 3], 2)

    def test_set_x(self):
        """..."""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, {1, 2, 3}, 2)

    def test_tuple_x(self):
        """..."""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, (1, 2, 3), 2)

    def test_frozenset_x(self):
        """..."""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, frozenset({1, 2, 3}))

    def test_range_x(self):
        """..."""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, range(5))

    def test_bytes_x(self):
        """..."""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, b"Python")

    def test_bytearray_x(self):
        """..."""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, bytearray(b"abcdefg"))

    def test_memoryview_x(self):
        """..."""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, memoryview(b"abcedfg"))

    def test_inf_x(self):
        """..."""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, float("inf"), 2)

    def test_nan_x(self):
        """..."""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, float("nan"), 2)

    def test_negative_x(self):
        """..."""
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(5, 3, -1, 0)


class TestRectangleY(unittest.TestCase):
    """Unittests for testing initialization of Rectangle y attribute."""

    def test_none_y(self):
        """..."""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, None)

    def test_str_y(self):
        """..."""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 1, "invalid")

    def test_float_y(self):
        """..."""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, 5.5)

    def test_complex_y(self):
        """..."""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, complex(5))

    def test_dict_y(self):
        """..."""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 1, {"a": 1, "b": 2})

    def test_list_y(self):
        """..."""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 1, [1, 2, 3])

    def test_set_y(self):
        """..."""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 1, {1, 2, 3})

    def test_tuple_y(self):
        """..."""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 1, (1, 2, 3))

    def test_frozenset_y(self):
        """..."""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, frozenset({1, 2, 3}))

    def test_range_y(self):
        """..."""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, range(5))

    def test_bytes_y(self):
        """..."""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, b"Python")

    def test_bytearray_y(self):
        """..."""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, bytearray(b"abcdefg"))

    def test_memoryview_y(self):
        """..."""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, memoryview(b"abcedfg"))

    def test_inf_y(self):
        """..."""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 1, float("inf"))

    def test_nan_y(self):
        """..."""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 1, float("nan"))

    def test_negative_y(self):
        """..."""
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(3, 5, 0, -1)


class TestRectangeInvalidArgType(unittest.TestCase):
    """Unittests for testing Rectangle with wrong argument types."""

    def test_width_before_height(self):
        """..."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("width", "height")

    def test_width_before_x(self):
        """..."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("width", 2, "x")

    def test_width_before_y(self):
        """..."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("width", 2, 3, "y")

    def test_height_before_x(self):
        """..."""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, "height", "x")

    def test_height_before_y(self):
        """..."""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, "height", 2, "y")

    def test_x_before_y(self):
        """..."""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, "x", "y")


class TestRectangleArea(unittest.TestCase):
    """Unittests for testing the area method of the Rectangle class."""

    def test_area_small(self):
        """..."""
        r = Rectangle(10, 2, 0, 0, 0)
        self.assertEqual(20, r.area())

    def test_area_one_arg(self):
        """..."""
        r = Rectangle(2, 10, 1, 1, 1)
        with self.assertRaises(TypeError):
            r.area(1)

    def test_area_large(self):
        """..."""
        r = Rectangle(999999999999999, 999999999999999999, 0, 0, 1)
        self.assertEqual(999999999999998999000000000000001, r.area())

    def test_area_changed_attributes(self):
        """..."""
        r = Rectangle(2, 10, 1, 1, 1)
        r.width = 7
        r.height = 14
        self.assertEqual(98, r.area())


class TestRectangleSTDOUT(unittest.TestCase):
    """Unittests for testing __str__ and display methods of Rectangle class."""

    @staticmethod
    def read_stdout(rect, method):
        """Reads and returns text printed to stabdard output.
        Args:
            rect (Rectangle): The Rectangle to print to stdout.
            method (str): The method to run on rect.
        Returns:
            The text printed to stdout by calling method on sq.
        """
        extr = io.StringIO()
        sys.stdout = extr
        if method == "print":
            print(rect)
        else:
            rect.display()
        sys.stdout = sys.__stdout__
        return extr

    # Test __str__ method
    def test_str_method_print_width_height(self):
        """..."""
        r = Rectangle(4, 6)
        capture = TestRectangleSTDOUT.read_stdout(r, "print")
        correct = f"[Rectangle] ({r.id}) 0/0 - 4/6\n"
        self.assertEqual(correct, capture.getvalue())

    def test_str_method_width_height_x(self):
        """..."""
        r = Rectangle(5, 5, 1)
        correct = f"[Rectangle] ({r.id}) 1/0 - 5/5"
        self.assertEqual(correct, r.__str__())

    def test_str_method_width_height_x_y(self):
        """..."""
        r = Rectangle(1, 8, 2, 4)
        correct = f"[Rectangle] ({r.id}) 2/4 - 1/8"
        self.assertEqual(correct, str(r))

    def test_str_method_width_height_x_y_id(self):
        """..."""
        r = Rectangle(13, 21, 2, 4, 7)
        self.assertEqual("[Rectangle] (7) 2/4 - 13/21", str(r))

    def test_str_method_changed_attributes(self):
        """..."""
        r = Rectangle(7, 7, 0, 0, [4])
        r.width = 15
        r.height = 1
        r.x = 8
        r.y = 10
        self.assertEqual("[Rectangle] ([4]) 8/10 - 15/1", str(r))

    def test_str_method_one_arg(self):
        """..."""
        r = Rectangle(1, 2, 3, 4, 5)
        with self.assertRaises(TypeError):
            r.__str__(1)

    # Test display method
    def test_display_width_height(self):
        """..."""
        r = Rectangle(2, 3, 0, 0, 0)
        capture = TestRectangleSTDOUT.read_stdout(r, "display")
        self.assertEqual("##\n##\n##\n", capture.getvalue())

    def test_display_width_height_x(self):
        """..."""
        r = Rectangle(3, 2, 1, 0, 1)
        capture = TestRectangleSTDOUT.read_stdout(r, "display")
        self.assertEqual(" ###\n ###\n", capture.getvalue())

    def test_display_width_height_y(self):
        """..."""
        r = Rectangle(4, 5, 0, 1, 0)
        capture = TestRectangleSTDOUT.read_stdout(r, "display")
        display = "\n####\n####\n####\n####\n####\n"
        self.assertEqual(display, capture.getvalue())

    def test_display_width_height_x_y(self):
        """..."""
        r = Rectangle(2, 4, 3, 2, 0)
        capture = TestRectangleSTDOUT.read_stdout(r, "display")
        display = "\n\n   ##\n   ##\n   ##\n   ##\n"
        self.assertEqual(display, capture.getvalue())

    def test_display_one_arg(self):
        """..."""
        r = Rectangle(5, 1, 2, 4, 7)
        with self.assertRaises(TypeError):
            r.display(1)


class TestRectangleUpdateArgs(unittest.TestCase):
    """Unit tests for testing the update args method of the Rectangle class."""

    def setUp(self):
        """Set up a Rectangle instance for testing."""
        self.rectangle = Rectangle(10, 10, 10, 10, 10)

    def test_update_args_zero(self):
        """Test update with zero arguments."""
        self.rectangle.update()
        self.assertEqual("[Rectangle] (10) 10/10 - 10/10", str(self.rectangle))

    def test_update_args_one(self):
        """Test update with one argument."""
        self.rectangle.update(89)
        self.assertEqual("[Rectangle] (89) 10/10 - 10/10", str(self.rectangle))

    def test_update_args_two(self):
        """Test update with two arguments."""
        self.rectangle.update(89, 2)
        self.assertEqual("[Rectangle] (89) 10/10 - 2/10", str(self.rectangle))

    def test_update_args_three(self):
        """Test update with three arguments."""
        self.rectangle.update(89, 2, 3)
        self.assertEqual("[Rectangle] (89) 10/10 - 2/3", str(self.rectangle))

    def test_update_args_four(self):
        """Test update with four arguments."""
        self.rectangle.update(89, 2, 3, 4)
        self.assertEqual("[Rectangle] (89) 4/10 - 2/3", str(self.rectangle))

    def test_update_args_five(self):
        """Test update with five arguments."""
        self.rectangle.update(89, 2, 3, 4, 5)
        self.assertEqual("[Rectangle] (89) 4/5 - 2/3", str(self.rectangle))

    def test_update_args_none_id(self):
        """Test update with None value for id."""
        self.rectangle.update(None)
        correct = f"[Rectangle] ({self.rectangle.id}) 10/10 - 10/10"
        self.assertEqual(correct, str(self.rectangle))

    def test_update_args_none_id_and_more(self):
        """Test update with None value for id and additional arguments."""
        self.rectangle.update(None, 4, 5, 2)
        correct = f"[Rectangle] ({self.rectangle.id}) 2/10 - 4/5"
        self.assertEqual(correct, str(self.rectangle))

    def test_update_args_twice(self):
        """Test update with arguments called twice."""
        self.rectangle.update(89, 2, 3, 4, 5, 6)
        self.rectangle.update(6, 5, 4, 3, 2, 89)
        self.assertEqual("[Rectangle] (6) 3/2 - 5/4", str(self.rectangle))

    def test_update_args_invalid_width_type(self):
        """Test update with invalid type for width."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            self.rectangle.update(89, "invalid")

    def test_update_args_width_zero(self):
        """Test update with width value of zero."""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            self.rectangle.update(89, 0)

    def test_update_args_width_negative(self):
        """Test update with negative width value."""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            self.rectangle.update(89, -5)

    def test_update_args_invalid_height_type(self):
        """Test update with invalid type for height."""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            self.rectangle.update(89, 2, "invalid")

    def test_update_args_height_zero(self):
        """Test update with height value of zero."""
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            self.rectangle.update(89, 1, 0)

    def test_update_args_height_negative(self):
        """Test update with negative height value."""
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            self.rectangle.update(89, 1, -5)

    def test_update_args_invalid_x_type(self):
        """Test update with invalid type for x."""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            self.rectangle.update(89, 2, 3, "invalid")

    def test_update_args_x_negative(self):
        """Test update with negative x value."""
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            self.rectangle.update(89, 1, 2, -6)

    def test_update_args_invalid_y(self):
        """Test update with invalid type for y."""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            self.rectangle.update(89, 2, 3, 4, "invalid")

    def test_update_args_y_negative(self):
        """Test update with negative y value."""
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            self.rectangle.update(89, 1, 2, 3, -6)

    def test_update_args_width_before_height(self):
        """Test update with width specified before height."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            self.rectangle.update(89, "invalid", "invalid")

    def test_update_args_width_before_x(self):
        """Test update with width specified before x."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            self.rectangle.update(89, "invalid", 1, "invalid")

    def test_update_args_width_before_y(self):
        """Test update with width specified before y."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            self.rectangle.update(89, "invalid", 1, 2, "invalid")

    def test_update_args_height_before_x(self):
        """Test update with height specified before x."""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            self.rectangle.update(89, 1, "invalid", "invalid")

    def test_update_args_height_before_y(self):
        """Test update with height specified before y."""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            self.rectangle.update(89, 1, "invalid", 2, "invalid")

    def test_update_args_x_before_y(self):
        """Test update with x specified before y."""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            self.rectangle.update(89, 1, 2, "invalid", "invalid")


class TestRectangleUpdateKwargs(unittest.TestCase):
    """
    Unit tests for testing the update kwargs method of the Rectangle class.
    """

    def setUp(self):
        """Set up a Rectangle instance for testing."""
        self.rectangle = Rectangle(10, 10, 10, 10, 10)

    def test_update_kwargs_one(self):
        """Test update with one keyword argument."""
        self.rectangle.update(id=1)
        self.assertEqual("[Rectangle] (1) 10/10 - 10/10", str(self.rectangle))

    def test_update_kwargs_two(self):
        """Test update with two keyword arguments."""
        self.rectangle.update(width=2, id=1)
        self.assertEqual("[Rectangle] (1) 10/10 - 2/10", str(self.rectangle))

    def test_update_kwargs_three(self):
        """Test update with three keyword arguments."""
        self.rectangle.update(width=2, height=3, id=89)
        self.assertEqual("[Rectangle] (89) 10/10 - 2/3", str(self.rectangle))

    def test_update_kwargs_four(self):
        """Test update with four keyword arguments."""
        self.rectangle.update(id=89, x=1, height=2, y=3, width=4)
        self.assertEqual("[Rectangle] (89) 1/3 - 4/2", str(self.rectangle))

    def test_update_kwargs_five(self):
        """Test update with five keyword arguments."""
        self.rectangle.update(y=5, x=8, id=99, width=1, height=2)
        self.assertEqual("[Rectangle] (99) 8/5 - 1/2", str(self.rectangle))

    def test_update_kwargs_none_id(self):
        """Test update with None value for id."""
        self.rectangle.update(id=None)
        correct = f"[Rectangle] ({self.rectangle.id}) 10/10 - 10/10"
        self.assertEqual(correct, str(self.rectangle))

    def test_update_kwargs_none_id_and_more(self):
        """Test update with None value for id and other keyword arguments."""
        self.rectangle.update(id=None, height=7, y=9)
        correct = f"[Rectangle] ({self.rectangle.id}) 10/9 - 10/7"
        self.assertEqual(correct, str(self.rectangle))

    def test_update_kwargs_twice(self):
        """Test update with keyword arguments called twice."""
        self.rectangle.update(id=89, x=1, height=2)
        self.rectangle.update(y=3, height=15, width=2)
        self.assertEqual("[Rectangle] (89) 1/3 - 2/15", str(self.rectangle))

    def test_update_kwargs_invalid_width_type(self):
        """Test update with invalid width type."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            self.rectangle.update(width="invalid")

    def test_update_kwargs_width_zero(self):
        """Test update with width zero."""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            self.rectangle.update(width=0)

    def test_update_kwargs_width_negative(self):
        """Test update with negative width value."""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            self.rectangle.update(width=-5)

    def test_update_kwargs_invalid_height_type(self):
        """Test update with invalid height type."""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            self.rectangle.update(height="invalid")

    def test_update_kwargs_height_zero(self):
        """Test update with height zero."""
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            self.rectangle.update(height=0)

    def test_update_kwargs_height_negative(self):
        """Test update with negative height value."""
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            self.rectangle.update(height=-5)

    def test_update_kwargs_invalid_x_type(self):
        """Test update with invalid x type."""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            self.rectangle.update(x="invalid")

    def test_update_kwargs_x_negative(self):
        """Test update with negative x value."""
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            self.rectangle.update(x=-5)

    def test_update_kwargs_invalid_y_type(self):
        """Test update with invalid y type."""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            self.rectangle.update(y="invalid")

    def test_update_kwargs_y_negative(self):
        """Test update with negative y value."""
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            self.rectangle.update(y=-5)

    def test_update_args_and_kwargs(self):
        """Test update with both positional and keyword arguments."""
        self.rectangle.update(89, 2, height=4, y=6)
        self.assertEqual("[Rectangle] (89) 10/10 - 2/10", str(self.rectangle))

    def test_update_kwargs_wrong_keys(self):
        """Test update with wrong keyword arguments."""
        self.rectangle.update(a=5, b=10)
        self.assertEqual("[Rectangle] (10) 10/10 - 10/10", str(self.rectangle))

    def test_update_kwargs_some_wrong_keys(self):
        """Test update with some wrong keyword arguments."""
        self.rectangle.update(height=5, id=89, a=1, b=54, x=19, y=7)
        self.assertEqual("[Rectangle] (89) 19/7 - 10/5", str(self.rectangle))


class TestRectangleToDictionary(unittest.TestCase):
    """
    Unit tests for testing the to_dictionary method of the Rectangle class.
    """

    def setUp(self):
        self.rect = Rectangle(10, 2, 1, 9, 5)

    def test_to_dictionary_output(self):
        """
        Test if the to_dictionary method returns the correct dictionary
        output.
        """
        expected_output = {"x": 1, "y": 9, "id": 5, "height": 2, "width": 10}
        self.assertDictEqual(expected_output, self.rect.to_dictionary())

    def test_to_dictionary_no_object_changes(self):
        """
        Test if the to_dictionary method does not modify the original
        object.
        """
        rect_a = Rectangle(5, 9, 1, 2, 10)
        rect_a.update(**self.rect.to_dictionary())
        self.assertNotEqual(self.rect, rect_a)

    def test_to_dictionary_with_argument(self):
        """
        Test if TypeError is raised when passing an argument
        to the to_dictionary method.
        """
        with self.assertRaises(TypeError):
            self.rect.to_dictionary(1)


class TestRectangleCreate(unittest.TestCase):
    """
    Unit tests for testing the create method of the Rectangle class
    inherited from the Base class.
    """

    def test_rectangle_create_1_arg(self):
        """
        Test if the create method returns a new Rectangle instance
        with one attribute updated.
        """
        rect = Rectangle.create(**{'id': 89, 'width': 1})
        self.assertIsInstance(rect, Rectangle)

    def test_rectangle_create_2_args(self):
        """
        Test if the create method returns a new Rectangle instance
        with two attributes updated.
        """
        rect = Rectangle.create(**{'id': 76, 'width': 112})
        self.assertEqual(rect.id, 76)
        self.assertEqual(rect.width, 112)

    def test_rectangle_create_3_args(self):
        """
        Test if the create method returns a new Rectangle instance
        with three attributes updated.
        """
        rect = Rectangle.create(**{'id': 24, 'width': 25, 'height': 11})
        self.assertEqual(rect.id, 24)
        self.assertEqual(rect.width, 25)
        self.assertEqual(rect.height, 11)

    def test_rectangle_create_4_args(self):
        """
        Test if the create method returns a new Rectangle instance
        with four attributes updated.
        """
        rect = Rectangle.create(**{'id': 89, 'width': 1, 'height': 2, 'x': 3})
        self.assertEqual(rect.id, 89)
        self.assertEqual(rect.width, 1)
        self.assertEqual(rect.height, 2)
        self.assertEqual(rect.x, 3)

    def test_rectangle_create_5_args(self):
        """
        Test if the create method returns a new Rectangle instance
        with five attributes updated.
        """
        rect = Rectangle.create(**{'id': 89, 'width': 1, 'height': 2, 'x': 3,
                                   'y': 4})
        self.assertEqual(rect.id, 89)
        self.assertEqual(rect.width, 1)
        self.assertEqual(rect.height, 2)
        self.assertEqual(rect.x, 3)
        self.assertEqual(rect.y, 4)


class RectangleSaveToFile(unittest.TestCase):
    """
    Unit tests for testing the save_to_file method of the Rectangle class.
    """

    def test_rectangle_save_to_file_none(self):
        """
        Test the save_to_file method with default.
        """
        Rectangle.save_to_file(None)
        self.assertTrue(Path("Rectangle.json").is_file())
        objs = Rectangle.load_from_file()
        self.assertEqual(len(objs), 0)

    def test_rectangle_save_to_file_empty_list(self):
        """
        Test method for testing the save_to_file method with nothing.
        """
        Rectangle.save_to_file([])
        objs = Rectangle.load_from_file()
        self.assertEqual(len(objs), 0)
        self.assertIsInstance(objs, list)

    def test_rectangle_save_to_file_list(self):
        """
        Test method for testing the save_to_file method with a list.
        """
        Rectangle.save_to_file([Rectangle(1, 2, 3, 4, 5)])
        objs = Rectangle.load_from_file()
        self.assertEqual(len(objs), 1)
        self.assertIsInstance(objs[0], Rectangle)
        self.assertEqual(objs[0].id, 5)
        self.assertEqual(objs[0].width, 1)
        self.assertEqual(objs[0].height, 2)
        self.assertEqual(objs[0].x, 3)
        self.assertEqual(objs[0].y, 4)


class TestRectangleLoadFromFile(unittest.TestCase):
    """Unit tests for testing the load_from_file method of Rectangle."""

    def setUp(self):
        """
        Removes the Rectangle.json file if it exists.
        """
        if Path("Rectangle.json").is_file():
            Path("Rectangle.json").unlink()

    def test_rectangle_load_from_file_no_file(self):
        """
        Test the load_from_file method with missing Rectangle.json file.
        """
        self.assertFalse(Path("Rectangle.json").is_file())
        self.assertEqual(Rectangle.load_from_file(), [])

    def test_rectangle_load_from_existing_file(self):
        """
        Test the load_from_file method with existing Rectangle.json file.
        """
        Rectangle.save_to_file([Rectangle(1, 2, 3, 4, 5)])
        objs = Rectangle.load_from_file()
        self.assertEqual(len(objs), 1)
        self.assertIsInstance(objs[0], Rectangle)
        self.assertEqual(objs[0].id, 5)
        self.assertEqual(objs[0].width, 1)
        self.assertEqual(objs[0].height, 2)
        self.assertEqual(objs[0].x, 3)
        self.assertEqual(objs[0].y, 4)


if __name__ == "__main__":
    unittest.main()
