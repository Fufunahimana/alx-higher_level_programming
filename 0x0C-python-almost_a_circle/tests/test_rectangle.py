#!/usr/bin/python3

""" Unittest for rectangle class """

import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """ Rectangle class unittest """

    def test_id(self):
        r = Rectangle(10, 9, 0, 0, 11)
        self.assertEqual(r.id, 11)

    def test_sides(self):
        r = Rectangle(10, 8, 4, 2)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 8)
        self.assertEqual(r.x, 4)
        self.assertEqual(r.y, 2)

    def test_exceptions(self):
        with self.assertRaises(TypeError):
            r = Rectangle('one', 10)

        with self.assertRaises(TypeError):
            r = Rectangle(3, 'one')

        with self.assertRaises(TypeError):
            r = Rectangle(3, 4, 'one', 3)

        with self.assertRaises(TypeError):
            r = Rectangle(3, 5, 1, 'one')

        with self.assertRaises(ValueError):
            r = Rectangle(0, 4)

        with self.assertRaises(ValueError):
            r = Rectangle(-3, 4)

        with self.assertRaises(ValueError):
            r = Rectangle(3, 0)

        with self.assertRaises(ValueError):
            r = Rectangle(3, -9)

        with self.assertRaises(ValueError):
            r = Rectangle(3, 5, -3, 4)

        with self.assertRaises(ValueError):
            r = Rectangle(3, 4, 4, -8)

    def test_area(self):
        r = Rectangle(4, 10)
        self.assertEqual(r.area(), 40)

    def test_str(self):
        r = Rectangle(4, 6, 2, 1, 12)
        result = str(r)

        output = "[Rectangle] (12) 2/1 - 4/6"

        self.assertEqual(result, output)

    def test_update(self):
        r = Rectangle(10, 10, 10, 10, 20)
        result = str(r)
        output = "[Rectangle] (20) 10/10 - 10/10"
        self.assertEqual(result, output)

        r.update(89)
        result = str(r)
        output = "[Rectangle] (89) 10/10 - 10/10"
        self.assertEqual(result, output)

        r.update(89, 2)
        result = str(r)
        output = "[Rectangle] (89) 10/10 - 2/10"
        self.assertEqual(result, output)

    def test_update_kwargs(self):
        r2 = Rectangle(10, 10, 10, 10, 30)
        r2.update(width=1, x=2)
        result = str(r2)
        output = "[Rectangle] (30) 2/10 - 1/10"
        self.assertEqual(result, output)


    def test_display(self):
        r = Rectangle(2, 2)

        result = r.display()
        output = "##\n##\n"

        self.assertEqual(result, output)

        r1 = Rectangle(2, 3, 2, 2)
        result = r1.display()
        output = "\n\n  ##\n  ##\n  ##\n"

        self.assertEqual(result, output)
