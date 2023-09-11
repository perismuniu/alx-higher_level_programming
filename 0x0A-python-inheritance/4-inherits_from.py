#!/usr/bin/python3
""" Defines an inherited class-checking function"""


def inherits_from(obj, a_class):
    """
    Check if the object is an instance of
    a class that inherited (directly or indirectly)
    from the specified class.

    Args:
        obj: The object to check.
        a_class: The specified class to check against.

    Returns:
        bool: True if obj is an instance of
        a subclass of a_class, False otherwise.
    """
    current_class = type(obj)

    while current_class is not None:
        if a_class in current_class.__bases__:
            return True
        current_class = current_class.__base__
    return False
