#!/usr/bin/python3
# 6-max_integer_test.py
"""Unittests for a function max_integer([..])."""

import unittest
max_int = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    class for testing 6-max_integer_test.py
    """

    def test_max_integer(self):
        """
        Test for positive integers
        """
        test_list = [1, 2, 3, 5, 4]
        self.assertEqual(max_int(test_list), 5)

    def test_max_integer_neg(self):
        """ 
        Test for negative integers
        """
        test_list = [1, -12, -3, -8, -24, -40, -400, -12, 0]
        self.assertEqual(max_int(test_list), 1)

    def test_max_integer_(self):
        """ 
        Test for an empty list
        """
        self.assertEqual(max_int([]), None)
