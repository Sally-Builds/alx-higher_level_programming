#!/usr/bin/python3

"""
Module: This module defines a function that divides a numbers in a list of list by another number
"""

def matrix_divided(matrix, div):
    """divides the number in a list of list by another number

    Args:
        matrix(list): list of list to divide
        div(int): number to divide the elements of the list with
    
    Return: new list of the divided list of list

    Raise:
        TypeError: if matrix is not a list of list of numbers
        ZeroDivisionError: if the argument div is zero
    """
    result = []

    if not isinstance(matrix, list) or matrix == []:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    for i in range(len(matrix)):
        if not isinstance(matrix[i], list):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if (i + 1) < len(matrix):
            if len(matrix[i]) != len(matrix[i + 1]):
                raise TypeError("Each row of the matrix must have the same size")
        result.append([])
        for j in range(len(matrix[i])):
            if type(div) not in [float, int]:
                raise TypeError("div must be a number")
            if div == 0:
                raise ZeroDivisionError("division by zero")

            result[i].append(round(matrix[i][j] / div, 2))

    return result
