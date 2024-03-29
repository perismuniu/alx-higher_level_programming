#!/usr/bin/python3
"""Defines a function that adds a new attribute to an object"""


def add_attribute(obj, attr_name, attr_value):
    """
    Adds a new attribute to an object if it's possible.

    Args:
        obj: The object to which the attribute should be added.
        attr_name: The name of the new attribute.
        attr_value: The value of the new attribute.

    Raises:
        TypeError: If the object cannot have new attributes,
        a TypeError is raised with the message "Can't add new attribute."
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("Can't add new attribute")
    setattr(obj, attr_name, attr_value)
