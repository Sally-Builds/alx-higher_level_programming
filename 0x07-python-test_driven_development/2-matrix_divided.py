#!/usr/bin/python3
"""
This module defines a matrix division function
"""

def matrix_divided(matrix, div):
    """This function divides all elements of a matrix by a given number
    Args:
        matrix: A list of lists (matrix)- members can be of type ints or floats
        div: Number to be used for the division (can be a float or an integer)
    Raises:
        TypeError: If the matrix contains non-numbers
        TypeError: If the matrix contains rows of different sizes
        TypeError: If div is not an int or float
        ZeroDivisionError: If div is 0
    Returns:
        A new matrix which represents the result of the divisions
    """
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
