#!/usr/bin/python3
def add_integer(a, b=98):
    """Returns an integer: the addition of a and b
        Args:
            'a' and 'b' must be first casted to integers if they are float.

        Raise:
            Type error if a and b if are not integers or floats.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    result = a + b
    return result
