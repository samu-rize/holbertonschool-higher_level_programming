#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix[0]:
        print()
    lenx = len(matrix)
    for x in range(lenx):
        leny = len(matrix[x])
        for y in range(leny):
            if y == leny - 1:
                print('{:d}'.format(matrix[x][y]))
            else:
                print('{:d}'.format(matrix[x][y]), end=' ')
