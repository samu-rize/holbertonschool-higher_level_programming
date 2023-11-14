#!/usr/bin/python3
"""module contain a functions to divides all elements of a matrix"""


def matrix_divided(matrix, div):
    """functions divides all elements of a matrix"""
    new_matrix = []

    if not matrix:
        return new_matrix

    row_size = len(matrix[0])

    if not (isinstance(div, int) or isinstance(div, float)):
        raise TypeError ("div must be a number")
    if div == 0:
        raise ZeroDivisionError ("division by zero")

    for i in range(len(matrix)):

        if row_size != len(matrix[i]):
            raise TypeError ("Each row of the matrix must have the same size")

        new_row = []
        for j in range(len(matrix[i])):

            if not (isinstance(matrix[i][j], int) or isinstance(matrix[i][j], float)):
                raise TypeError ("matrix must be a matrix (list of lists) of integers/floats")

            new_row.append(round(matrix[i][j] / div, 2))
        new_matrix.append(new_row)

    return new_matrix
