#!/usr/bin/python3
"""Defines function that writes a string to a text file (UTF8)"""


def write_file(filename="", text=""):
    """
     Write a string to a text file (UTF8) and return
     the number of characters written.

     Args:
        filename (str): The name of the file to write to.
        text (str): The text to write to the file.

     Returns:
        int: The number of characters written.

    This function creates the file if it doesn't exist
    and overwrites its content if it already exists.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        num_characters_written = file.write(text)
    return num_characters_written
