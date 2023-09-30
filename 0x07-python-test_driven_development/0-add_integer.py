#!/usr/bin/python3
"""
Module: 0-add_integer

This module performs mathematical operation addition
"""

def add_integer(a, b=98):
    """ 
    Adds two integers and returns the result

    Args: 
        a (int or float): The first number to be added
        b (int or float, optional): The other number to add

    Return:
        int: The sum of a and b as an integer

    Raises:
        TypeError: if 'a' or 'b' is not of type int or float.
    """
    if type(a) not in [float, int]:
        raise TypeError("a must be an integer")
    elif type(b) not in [float, int]:
        raise TypeError("b must be an integer")

    return int(a) + int(b)
