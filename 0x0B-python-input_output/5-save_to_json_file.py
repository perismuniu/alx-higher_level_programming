#!/usr/bin/python3
"""Defines function that writes an object to a text file using JSON"""
import json


def save_to_json_file(my_obj, filename):
    """
    Serialize and save an object to a JSON file.

    :param my_obj: The object to be serialized and saved.
    :type my_obj: object
    :param filename: The name of the file to which the object will be saved.
    :type filename: str
    """
    with open(filename, 'w') as json_file:
        json.dump(my_obj, json_file)
