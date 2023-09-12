#!/usr/bin/python3
"""Defines function that returns JSON representation of an object (string)"""
import json


def to_json_string(my_obj):
    """
    Convert an object to its JSON representation.

    :param my_obj: The object to be converted to JSON.
    :return: JSON representation of the object as a string.
    """
    return json.dumps(my_obj)
