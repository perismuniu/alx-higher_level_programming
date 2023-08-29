#!/usr/bin/python3
"""Define a class square"""


class Square:
    """Represents a square"""

    def __init__(self, size=0):
        """Initialize a new square instance"""
        self.__size = size

        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")
