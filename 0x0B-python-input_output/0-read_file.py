#!/usr/bin/python3
"""Defines a function that reads a textfile (UTF8)"""


def read_file(filename=""):
    """
    Read a text file and print its contents to stdout.

    Args:
        filename (str, optional): The name of the file to be read.
        Defaults to an empty string.

    Returns:
        None
    """
    with open(filename, encoding='utf-8') as file:
        print(file.read(), end='')
