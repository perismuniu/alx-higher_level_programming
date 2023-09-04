#!/usr/bin/python3
def print_square(size):
    """
    Print a square of a given size using the '#' character.

    Args:
    size (int): The length of the sides of the square.

    Raises:
    TypeError: If size is not an integer.
    ValueError: If size is less than 0.

    Returns:
    None
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for j in range(size):
            print('#', end='')
        print()
