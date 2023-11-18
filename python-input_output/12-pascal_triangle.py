#!/usr/bin/python3
"""Generates Pascal's Triangle up to the specified number of rows."""


def pascal_triangle(n):
    """Generates Pascal's Triangle with 'n' rows."""
    if n < 1:
        return []

    triangles = [[1]]
    while len(triangles) < n:
        row = [1]
        while len(triangles) != len(row):
            row.append(triangles[-1][len(row)] + triangles[-1][len(row) - 1])
        row.append(1)
        triangles.append(row)
    return triangles
