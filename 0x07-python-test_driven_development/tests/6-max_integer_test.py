#!/usr/bin/python3
""" Unittest for max_integer([...]) """

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)

    def test_single_item(self):
        self.assertEqual(max_integer([6]), 6)

    def test_positive_int(self):
        self.assertEqual(max_integer([1, 4, 9]), 9)

    def test_negative_int(self):
        self.assertEqual(max_integer([-2, -4, -8]), -2)

    def test_mixed_nums(self):
        self.assertEqual(max_integer([10, -2, 0]), 10)

    def test_floats(self):
        self.assertEqual(max_integer([2.2, 2.1, 2.0]), 2.2)

    def test_large_nums(self):
        self.assertEqual(max_integer([2000000, 1000000, 999999]), 2000000)
