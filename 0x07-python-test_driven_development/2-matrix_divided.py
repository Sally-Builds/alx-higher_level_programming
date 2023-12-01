#!/usr/bin/python3


def matrix_divided(matrix, div):
    if (not isinstance(div, int) and not isinstance(div, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) of integers/float")

    new_list = []
    for i in range(len(matrix)):
        if not isinstance(matrix[i], list):
            raise TypeError("matrix must be a matrix (list of lists) of integers/float")

        if i > 0:
            if len(matrix[i]) != len(matrix[i - 1]):
                raise TypeError("Each row of the matrix must have the same size")

        new_list.append([])
        for j in range(len(matrix[i])):
            if (not isinstance(matrix[i][j], int) and not isinstance(matrix[i][j], float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/float")
            new_list[i].append(round((matrix[i][j] / div), 2))

    return new_list
