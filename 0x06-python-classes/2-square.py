#!/usr/bin/python3
""" Square Module """


class Square:
    ''' Square '''
    def __init__(self, size=0):
        """Constructor for class Square"""
        try:
            if size <= 0:
                raise ValueError("size must be >= 0")
            if not isinstance(size, int):
                raise TypeError("size must be an integer")
            self.__size = size
        except Exception as e:
            print(e)
