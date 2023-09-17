#!/usr/bin/python3
import unittest

from models.base import Base


class TestBase(unittest.TestCase):
    

    def test_init_with_id(self):
        base = Base(10)
        self.assertEqual(base.id, 10)

    def test_init_without_id(self):
        base = Base()
        self.assertEqual(base.id, 1)

    def test_nb_objects_increments_correctly(self):
        base1 = Base()
        base2 = Base()
        self.assertEqual(base2.id, base1.id + 1)


if __name__ == '__main__':
    unittest.main()
