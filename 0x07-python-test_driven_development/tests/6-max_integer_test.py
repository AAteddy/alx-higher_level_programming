#!/usr/bin/python3
# 6-max_integer_test.py
"""Unittests for a function max_integer([..])."""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Define unittests for the function max_integer([..])."""

    def test_empty_list(self):
        """Test an empty list."""
        empty = []
        self.assertEqual(max_integer(empty), None)

    def test_single_element_list(self):
        """Test a list with a single element."""
        single_element = [2]
        self.assertEqual(max_integer(single_element), 2)

    def test_ordered_list(self):
        """Test an ordered list of integers."""
        ordered = [1, 2, 3, 4]
        self.assertEqual(max_integer(ordered), 4)

    def test_unordered_list(self):
        """Test an unordered list of integers."""
        unordered = [1, 3, 4, 2]
        self.assertEqual(max_integer(unordered), 4)

    def test_max_at_beginning(self):
        """Test a list with a beginning max value."""
        max_at_beginning = [4, 3, 2, 1]
        self.assertEqual(max_integer(max_at_beginning), 4)

    def test_float(self):
        """Test a list of floats."""
        floats = [1.1, 3.91, 7.05, 99.99]
        self.assertEqual(max_integer(floats), 99.99)

    def test_int_float(self):
        """Test a list of ints and floats."""
        ints_and_floats = [1.99, -10, 7.02, 11.01]
        self.assertEqual(max_integer(ints_and_floats), 11.01)

    def test_string(self):
        """Test a string."""
        string = "Teddy"
        self.assertEqual(max_integer(string), 'z')

    def test_list_strings(self):
        """Test a list of strings."""
        strings = ["Teddy", "Matty", "Abel", "Zed"]
        self.assertEqual(max_integer(strings), "Zed")

    def test_empty_string(self):
        """Test an empty string."""
        self.assertEqual(max_integer(""), None)

if __name__ == '__main__':
    unittest.main()

