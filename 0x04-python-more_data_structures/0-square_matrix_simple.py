#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix is None:
        return
    matrix = [[elem**2 for elem in row] for row in matrix]
    return matrix
