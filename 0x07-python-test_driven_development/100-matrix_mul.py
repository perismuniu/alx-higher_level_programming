#!/usr/bin/python3
def matrix_mul(m_a, m_b):
    """
    Multiply two matrices.

    Args:
        m_a: The first matrix.
        m_b: The second matrix.

    Returns:
        The product of the two matrices.

    Raises:
        TypeError: If m_a or m_b is not a list of lists.
        TypeError: If m_a or m_b is empty.
        TypeError: If one element of those list 
        of lists is not an integer or a float.
        TypeError: If m_a or m_b is not a rectangle 
        (all ‘rows’ should be of the same size).
        ValueError: If m_a and m_b can’t be multiplied.
    """

    if not isinstance(m_a, list) or not isinstance(m_b, list):
        raise TypeError("m_a must be a list or m_b must be a list")

    if not all(isinstance(row, list) for row in m_a) or not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_a must be a list of lists or m_b must be a list of lists")
    if not m_a or not m_b:
        raise ValueError("m_a can't be empty or m_b can't be empty")

    for row in m_a:
        if not all(isinstance(element, (int, float)) for element in row):
            raise TypeError("m_a should contain only integers or floats")

    for row in m_b:
        if not all(isinstance(element, (int, float)) for element in row):
            raise TypeError("m_b should contain only integers or floats")

    num_cols_a = len(m_a[0])
    num_rows_b = len(m_b)
    if not all(len(row) == num_cols_a for row in m_a) or not all(len(row) == num_rows_b for row in m_b):
        raise ValueError("Each row of m_a must be of the same size or each row of m_b must be of the same size")

    if num_cols_a != num_rows_b:
        raise ValueError("m_a and m_b can't be multiplied")

    result = []
    for i in range(len(m_a)):
        row = []
        for j in range(len(m_b[0])):
            product = sum(m_a[i][k] * m_b[k][j] for k in range(len(m_a[0])))
            row.append(product)
            result.append(row)

    return result
