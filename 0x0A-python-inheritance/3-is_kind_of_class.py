#!/usr/bin/python3
""" Defines class checking function """


def is_kind_of_class(obj, a_class):
    """
    Check if the object is an instance of,
    or if it is an instance of a class that
    inherited from the specified class.

    Args:
        obj: The object to check.
        a_class: The specified class to check against.

    Returns:
        bool: True if obj is an instance of a_class
        or its subclasses, False otherwise.
    """
    current_class = type(obj)
    while current_class is not None:
        if current_class == a_class:
            return True
        current_class = current_class.__base__
    return False
