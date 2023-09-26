#!/usr/bin/python3
""" Square Module """


class Square:
    ''' Square '''
    def __init__(self, size=0):
        """
        Constructor for the Square class.

        Args:
            size (int): The size of the square. Must be a non-negative integer.

        Raises:
            ValueError: If the provided size is negative.
            TypeError: If the provided size is not an integer.

        """
        if size < 0:
            raise ValueError("size must be >= 0")
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        self.__size = size
