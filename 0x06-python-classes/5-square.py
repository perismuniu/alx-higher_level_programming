#!/usr/bin/python3
"""Define a class square"""


class Square:
    """Represents a square"""

    def __init__(self, size=0):
        """Initialize a new square instance"""
        self.size = size

    @property
    def size(self):
        """Retrieve the current size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square

        Args:
            value (int): The size value to set

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is negative.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """compute and return the area of the square"""
        return self.__size**2

    def my_print(self):
        """Print the square with '#' character"""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print('#' * self.__size)
