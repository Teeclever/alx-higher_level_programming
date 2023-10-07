#!/usr/bin/python3
"""Unit Test File for Max Integer Function"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Unit tests for the max_integer function."""

    def test_max_in_ordered_list(self):
        """Test when the maximum value is in an ordered list of integers."""
        ordered = [1, 2, 3, 4]
        self.assertEqual(max_integer(ordered), 4)

    def test_max_in_unordered_list(self):
        """Test when the maximum value is in an unordered list of integers."""
        unordered = [1, 2, 4, 3]
        self.assertEqual(max_integer(unordered), 4)

    def test_max_at_beginning(self):
        """Test when the maximum value is at the beginning of the list."""
        max_at_beginning = [4, 3, 2, 1]
        self.assertEqual(max_integer(max_at_beginning), 4)

    def test_empty_list(self):
        """Test when the list is empty."""
        empty = []
        self.assertEqual(max_integer(empty), None)

    def test_single_element_list(self):
        """Test when the list contains a single element."""
        one_element = [7]
        self.assertEqual(max_integer(one_element), 7)

    def test_list_of_floats(self):
        """Test when the list contains only floats."""
        floats = [1.53, 6.33, -9.123, 15.2, 6.0]
        self.assertEqual(max_integer(floats), 15.2)

    def test_list_of_ints_and_floats(self):
        """Test when the list contains a mixture of ints and floats."""
        ints_and_floats = [1.53, 15.5, -9, 15, 6]
        self.assertEqual(max_integer(ints_and_floats), 15.5)

    def test_string(self):
        """Test when the input is a string."""
        string = "Brennan"
        self.assertEqual(max_integer(string), 'r')

    def test_list_of_strings(self):
        """Test when the list contains strings."""
        strings = ["Brennan", "is", "my", "name"]
        self.assertEqual(max_integer(strings), "name")

    def test_empty_string(self):
        """Test when the input is an empty string."""
        self.assertEqual(max_integer(""), None)

    def test_negative_integers(self):
        """Test when the list contains negative integers."""
        negative_integers = [-10, -5, -7, -2]
        self.assertEqual(max_integer(negative_integers), -2)

    def test_duplicate_max_value(self):
        """Test when the list contains duplicate maximum values."""
        duplicates = [3, 2, 4, 2, 5, 5]
        self.assertEqual(max_integer(duplicates), 5)


if __name__ == '__main__':
    unittest.main()
