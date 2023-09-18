#!/usr/bin/python3
"""Defines unittests for base.py"""

import os
import unittest
from models.base import Base
from models.square import Square
from models.rectangle import Rectangle

class TestBase(unittest.TestCase):
    """unittests for testing instantation of base class"""
    def test_to_json_string_empty_list(self):
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_to_json_string_non_empty_list(self):
        data = [{"key1": "value1", "key2": "value2"}]
        expected_json = '[\n    {\n        "key1": "value1",\n        "key2": "value2"\n    }\n]'
        self.assertEqual(Base.to_json_string(data), expected_json)

    def test_save_to_file_with_empty_list(self):
        Base.save_to_file([])
        with open("Base.json", "r") as file:
            self.assertEqual(file.read(), "[]")

    def test_save_to_file_with_non_empty_list(self):
        data = [{"key1": "value1", "key2": "value2"}]
        Base.save_to_file(data)
        with open("Base.json", "r") as file:
            self.assertEqual(file.read(), '[\n    {\n        "key1": "value1",\n        "key2": "value2"\n    }\n]')

    def test_from_json_string_empty_string(self):
        self.assertEqual(Base.from_json_string(""), [])

    def test_from_json_string_non_empty_string(self):
        json_string = '[{"key1": "value1", "key2": "value2"}]'
        data = [{"key1": "value1", "key2": "value2"}]
        self.assertEqual(Base.from_json_string(json_string), data)

    def test_create_rectangle(self):
        dictionary = {"id": 1, "width": 2, "height": 3}
        rect = Rectangle.create(**dictionary)
        self.assertEqual(rect.id, 1)
        self.assertEqual(rect.width, 2)
        self.assertEqual(rect.height, 3)

    def test_create_square(self):
        dictionary = {"id": 1, "size": 2}
        square = Square.create(**dictionary)
        self.assertEqual(square.id, 1)
        self.assertEqual(square.size, 2)

    def test_load_from_file_json_file_exists(self):
        data = [{"id": 1, "width": 2, "height": 3}]
        Rectangle.save_to_file(data)  # Save to Rectangle.json
        loaded_data = Rectangle.load_from_file()  # Load from Rectangle.json
        self.assertEqual(loaded_data[0].id, 1)
        self.assertEqual(loaded_data[0].width, 2)
        self.assertEqual(loaded_data[0].height, 3)

    def test_load_from_file_json_file_not_found(self):
        loaded_data = Base.load_from_file()
        self.assertEqual(loaded_data, [])

    def test_save_to_file_csv_with_empty_list(self):
        Base.save_to_file_csv([])
        with open("Base.csv", "r") as file:
            self.assertEqual(file.read(), "")

    def test_save_to_file_csv_with_non_empty_list(self):
        data = [Rectangle(1, 2, 3, 4)]
        Base.save_to_file_csv(data)
        with open("Base.csv", "r") as file:
            self.assertEqual(file.read(), "1,2,3,4,0\n")


if __name__ == "__main__":
    unittest.main()
