#!/usr/bin/python3
import unittest

max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Unit tests for the max_integer function."""

    def test_empty_list(self):
        """Test when the input list is empty."""
        self.assertIsNone(max_integer([]))

    def test_single_element_list(self):
        """Test when the input list contains a single element."""
        self.assertEqual(max_integer([5]), 5)

    def test_positive_numbers(self):
        """Test when the input list contains positive numbers."""
        self.assertEqual(max_integer([1, 3, 2, 5, 4]), 5)

    def test_negative_numbers(self):
        """Test when the input list contains negative numbers."""
        self.assertEqual(max_integer([-1, -3, -2, -5, -4]), -1)

    def test_mixed_numbers(self):
        """
        Test when the input list contains
        mixed positive and negative numbers.
        """
        self.assertEqual(max_integer([-1, 3, 0, -5, 4]), 4)


if __name__ == '__main__':
    unittest.main()
