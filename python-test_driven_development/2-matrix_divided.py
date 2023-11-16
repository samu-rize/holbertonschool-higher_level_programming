#!/usr/bin/python3
"""
Matrix division function
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by    1- Each row of the matrix must be
    of the same size

    Parameters:
    - matrix: list of lists of integers or floats
    - div: number (integer or float), cannot be 0
    """
    if type(div) not in (int, float):
        raise ValueError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    if not all(
        isinstance(row, list) and
            all(isinstance(val, (int, float)) for val in row)
            for row in matrix):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    new_matrix = [[round(val / div, 2) for val in row] for row in matrix]

    return new_matrix


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")
