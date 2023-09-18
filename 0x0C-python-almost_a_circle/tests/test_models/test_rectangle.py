#!/usr/bin/python3
"""Defines unittests for models/rectangle.py"""

import io
import sys
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangleMethods(unittest.TestCase):

    def test_rectangle_creation(self):
        # Test creating a rectangle with valid parameters
        r = Rectangle(4, 5)
        self.assertEqual(r.width, 4)
        self.assertEqual(r.height, 5)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)

    def test_invalid_width(self):
        # Test creating a rectangle with an invalid width
        with self.assertRaises(ValueError):
            Rectangle(-1, 5)

    def test_invalid_height(self):
        # Test creating a rectangle with an invalid height
        with self.assertRaises(ValueError):
            Rectangle(4, -5)

    def test_invalid_x(self):
        # Test creating a rectangle with an invalid x-coordinate
        with self.assertRaises(ValueError):
            Rectangle(4, 5, -1)

    def test_invalid_y(self):
        # Test creating a rectangle with an invalid y-coordinate
        with self.assertRaises(ValueError):
            Rectangle(4, 5, 0, -1)

    def test_area_calculation(self):
        # Test calculating the area of a rectangle
        r = Rectangle(3, 6)
        self.assertEqual(r.area(), 18)

    def test_display_output(self):
        # Test displaying a rectangle
        r = Rectangle(2, 3, 1, 1)
        expected_output = "\n" \
                          " ##\n" \
                          " ##\n" \
                          " ##\n"
        import io
        from unittest.mock import patch
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            r.display()
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_string_representation(self):
        # Test getting a string representation of the rectangle
        r = Rectangle(4, 5, 2, 3, 1)
        self.assertEqual(str(r), "[Rectangle] (1) 2/3 - 4/5")

    def test_update_with_args(self):
        # Test updating attributes using arguments
        r = Rectangle(1, 1)
        r.update(2, 3, 4, 5, 6)
        self.assertEqual(r.id, 2)
        self.assertEqual(r.width, 3)
        self.assertEqual(r.height, 4)
        self.assertEqual(r.x, 5)
        self.assertEqual(r.y, 6)

    def test_update_with_kwargs(self):
        # Test updating attributes using keyword arguments
        r = Rectangle(1, 1)
        r.update(id=2, width=3, height=4, x=5, y=6)
        self.assertEqual(r.id, 2)
        self.assertEqual(r.width, 3)
        self.assertEqual(r.height, 4)
        self.assertEqual(r.x, 5)
        self.assertEqual(r.y, 6)

    def test_to_dictionary(self):
        # Test getting a dictionary representation of the rectangle
        r = Rectangle(4, 5, 2, 3, 1)
        expected_dict = {
            'id': 1,
            'width': 4,
            'height': 5,
            'x': 2,
            'y': 3
        }
        self.assertEqual(r.to_dictionary(), expected_dict)


if __name__ == '__main__':
    unittest.main()
