#!/usr/bin/python3
def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix by a divisor.

    Args:
        matrix (list of lists): The matrix to be divided.
        div (int or float): The divisor.

     Returns:
        TypeError: If the matrix is not a list of lists of integers/floats,
                    if each row of the matrix doesn't have the same size,
                    or if div is not a number (integer or float).
        ZeroDivisionError: If div is equal to 0.
    """
    if not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists)\
                of integers/floats")
    if not all(isinstance(x, (int, float)) for row in matrix for x in row):
        raise TypeError("matrix must be a matrix (list of lists)\
                of integers/floats")
    if len(set(len(row) for row in matrix)) > 1:
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    result = [[round(x / div, 2) for x in row] for row in matrix]

    return result
