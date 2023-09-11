#!/usr/bin/python3
"""Define a class BaseGeometry"""


class BaseGeometry:
    """
    This class defines a BaseGeometry.
    """
    def area(self):
        """
        Public instance method that raises an Exception with the message
        'area() is not implemented'.
        """
        raise Exception("area() is not implemented")
