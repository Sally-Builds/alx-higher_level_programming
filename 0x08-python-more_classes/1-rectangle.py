#!/usr/bin/python3
"""
    Module: Defines a Rectangle class
"""


class Rectangle:
    """ This class defines an empty rectangle"""
    def __init__(self, width=0, height=0):
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.width = width
        self.height = height

    def width(self):
        """ get width"""
        return self.width

    def width(self, value):
        """set width of rectangle"""
        if width < 0:
            raise ValueError("width must be >= 0")
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        self.width = value

    def width(self):
        """ get width"""
        return self.height

    def height(self, value):
        """setter height of rectangle"""
        if value < 0:
            raise ValueError("height must be >= 0")
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        self.height = value
