#!/usr/bin/python3
"""Defines a function thatappends a string at the end of text file (UTF8)"""


def append_write(filename="", text=""):
    """
    Append a string to the end of a text file (UTF8) and
    return the number of characters added.

    Args:
        filename (str): The name of the file to append to.
        text (str): The text to append to the file.

    Returns:
        int: The number of characters added.

    This function creates the file if it doesn't exist.
    """
    with open(filename, 'a', encoding='utf-8') as file:
        num_characters_added = file.write(text)
    return num_characters_added
