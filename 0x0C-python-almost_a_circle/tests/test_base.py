#!/usr/bin/python3

""" Unittests for base class """

import unittest

from models.base import Base

class TestBase(unittest.TestCase):

    def test_positive_id(self):
        my_obj = Base(10)
        self.assertEqual(my_obj.id, 10)

    def test_id_none(self):
        b1 = Base()
        b2 = Base()
        b3 = Base()

        self.assertEqual(b3.id, 3)


if __name__ == '__main__':
    unittest.main()
