#!/usr/bin/python3

""" Unit tests for squarepy """

import unittest
from models.square import Square

class TestSquare(unittest.TestCase):

    def test_size(self):
        s = Square(5)
        self.assertEqual(s.width, 5)

    def test_area(self):
        s = Square(5)
        self.assertEqual(s.area(), 25)
