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
    if not all(isinstance(row, list) and all(isinstance(val, (int, float)) for val in row) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Check if each row of the matrix has the same size
    if len(set(len(row) for row in matrix)) > 1:
        raise TypeError("Each row of the matrix must have the same size")

    # Check if div is a number (integer or float) and not equal to 0
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Divide all elements of the matrix by div and round to 2 decimal places
    result = [[round(val / div, 2) for val in row] for row in matrix]

    return result
