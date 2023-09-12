#!/usr/bin/python3
"""Defines function that returns dictionary description."""


def class_to_json(obj):
    """
    Serialize a Python object with serializable attributes to a dictionary.

    Args:
        obj: An instance of a class with serializable attributes.

    Returns:
        A dictionary representation of the object.
    """
    return obj.__dict__
