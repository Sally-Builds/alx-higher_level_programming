#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    matrix_square = []

    if len(matrix) > 0:
        for i in range(len(matrix)):
            row = []
            for j in range(len(matrix[i])):
                row.append(matrix[i][j] ** 2)
            matrix_square.append(row)
    return matrix_square
