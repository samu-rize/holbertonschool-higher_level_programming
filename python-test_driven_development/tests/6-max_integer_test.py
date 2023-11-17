#!/usr/bin/python3
"""Unitest for max integer"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """unitest for max_integer([..])"""

    def Test_no_arg(self):
        """test max integer with test_no_arg"""
        self.assertEqual(max_integer([]), None)

    def Test_Ascending_ordered_list(self):
        """test max integer with Test_Ascending_ordered_list"""
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)

    def Test_unordered_list(self):
        """test max integer with test_unordered_list"""
        self.assertEqual(max_integer([1, 4, 5, 2, 3]), 5)

    def Test_descending_ordered_list(self):
        """test max integer with Test_descending_ordered_list"""
        self.assertEqual(max_integer([5, 4, 3, 2, 1]), 5)

    def Test_one_element_list(self):
        """test max integer with Test_one_element_list"""
        self.assertEqual(max_integer([5]), 5)

    def test_list_of_float(self):
        """test max integer with test_list_of_float"""
        self.assertEqual(max_integer([1.2, 2.3, 3.4, 4.5]), 4.5)

    def test_list_of_int_float(self):
        """test max integer with test_list_of_int_float"""
        self.assertEqual(max_integer([1.2, 2.3, 3.4, 4.5, 1, 4, 5, 2, 3]), 5)

    def test_string(self):
        """test max integer with test_string"""
        self.assertEqual(max_integer("string"), "r")

    def test_list_of_string(self):
        """test max integer with test_list_of_string"""
        self.assertEqual(max_integer(["list", "of", "strings"]), "strings")

    def test_empty_string(self):
        """test max integer with test_empty_string"""
        self.assertEqual(max_integer(""), "strings")


if __name__ == "__main__":
    unittest.main()
