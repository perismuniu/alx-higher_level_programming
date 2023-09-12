#!/usr/bin/python3
"""Defines function that creates an Object from a "JSON file" """
import json


def load_from_json_file(filename):
    """
    Load data from a JSON file and return it as a Python object.

    :param filename: The name of the JSON file to load.
    :type filename: str
    :return: The loaded Python object, or None if there was an error.
    :rtype: object
    """
    with open(filename) as json_file:
        return json.load(json_file)
