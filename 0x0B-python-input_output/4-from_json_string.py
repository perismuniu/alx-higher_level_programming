#!/usr/bin/python3
"""Defines function that reeturn object represented by JSON string."""
import json


def from_json_string(my_str):
    """
    Convert a JSON string to a Python data structure (object).

    :param my_str: The JSON string to be converted.
    :return: Python data structure (object) represented by the JSON string.
    """
    return json.loads(my_str)
