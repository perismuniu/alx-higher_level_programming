#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    square_matrix = []
    for row in matrix:
        square_row = []
        for value in row:
            square_value = value**2
            square_row.append(square_value)
        square_matrix.append(square_row)
    return square_matrix
