#!/usr/bin/python3
def text_indentation(text):
    """
    Prints the given text with 2 new lines after each '.', '?', and ':',
    removing leading and trailing whitespace.

    :param text: A string containing the text to be processed.
    :type text: str
    :raises TypeError: If the input is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    index = 0

    while index < len(text) and text[index] == ' ':
        index += 1

    while index < len(text):
        print(text[index], end="")
        if text[index] == "\n" or text[index] in ".?:":
            if text[index] in ".?:":
                print("\n")
            index += 1
            while index < len(text) and text[index] == ' ':
                index += 1
            continue
        index += 1
