#!/usr/bin/python3
"""Defines a function to check a class"""


def is_same_class(obj, a_class):
    """
    Check if an object is exactly an instance of the specified class.

    Args:
        obj: The object to be checked.
        a_class: The class to compare the object against.

    Returns:
        bool: True if the object is an instance of
        the specified class; otherwise, False.
    """
    obj_class = type(obj)

    if obj_class == a_class:
        return True
    else:
        return False
