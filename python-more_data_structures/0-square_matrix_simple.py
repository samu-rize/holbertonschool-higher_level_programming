#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for sublist in matrix:
        new_sublist = []
        for element in sublist:
            new_sublist.append(element ** 2)
        new_matrix.append(new_sublist)
    return new_matrix
