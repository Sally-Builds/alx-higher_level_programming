#!/usr/bin/python3
"""
    Module: Defines a Rectangle class
"""


class Rectangle:
    """ This class defines an empty rectangle"""
    def __init__(self, width=0, height=0):
        """Initializing this rectangle class
        Args:
            width: represents the width of the rectangle
            height: represents the height of the rectangle
        Raises:
            TypeError: if size is not integer
            ValueError: if size is less than zero
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ get width"""
        return self.width

    @width.setter
    def width(self, value):
        """set width of rectangle"""
        if value < 0:
            raise ValueError("width must be >= 0")
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        self.__width = value

    @property
    def height(self):
        """ get width"""
        return self.height

    @height.setter
    def height(self, value):
        """setter height of rectangle"""
        if value < 0:
            raise ValueError("height must be >= 0")
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        self.__height = value
