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

    punctuation = ['.', '?', ':']
    lines = []

    for line in text.splitlines():
        lines.extend(line.strip().split('\n'))

    for line in lines:
        stripped_line = line.strip()
        if stripped_line:
            for char in stripped_line:
                print(char, end='')
                if char in punctuation:
                    print('\n')
            print()
