#!/usr/bin/python3
"""Defines unittests for models/square.py"""

import io
import sys
import unittest
from models.base import Base
from models.square import Square


class TestSquare(unittest.TestCase):

    def test_square_creation(self):
        square = Square(5)
        self.assertEqual(square.size, 5)
        self.assertEqual(square.x, 0)
        self.assertEqual(square.y, 0)
        self.assertIsNotNone(square.id)

    def test_square_str_representation(self):
        square = Square(5, 2, 3, 1)
        self.assertEqual(str(square), "[Square] (1) 2/3 - 5")

    def test_square_update_method_with_args(self):
        square = Square(5, 2, 3, 1)
        square.update(2, 7, 4, 6)
        self.assertEqual(square.id, 2)
        self.assertEqual(square.size, 7)
        self.assertEqual(square.x, 4)
        self.assertEqual(square.y, 6)

    def test_square_update_method_with_kwargs(self):
        square = Square(5, 2, 3, 1)
        square.update(id=2, size=7, x=4, y=6)
        self.assertEqual(square.id, 2)
        self.assertEqual(square.size, 7)
        self.assertEqual(square.x, 4)
        self.assertEqual(square.y, 6)

    def test_square_size_property(self):
        square = Square(5)
        self.assertEqual(square.size, 5)
        square.size = 8
        self.assertEqual(square.size, 8)

    def test_square_size_property_with_invalid_value(self):
        square = Square(5)
        with self.assertRaises(ValueError):
            square.size = -1

    def test_square_to_dictionary(self):
        square = Square(5, 2, 3, 1)
        expected_dict = {'id': 1, 'size': 5, 'x': 2, 'y': 3}
        self.assertEqual(square.to_dictionary(), expected_dict)

    def test_square_area(self):
        square = Square(4)
        self.assertEqual(square.area(), 16)

    def test_square_invalid_size_on_creation(self):
        with self.assertRaises(ValueError):
            Square(0)

    def test_square_invalid_size_property(self):
        square = Square(5)
        with self.assertRaises(ValueError):
            square.size = 0


if __name__ == '__main__':
    unittest.main()
