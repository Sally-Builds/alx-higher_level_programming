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
        return self.__width

    @width.setter
    def width(self, value):
        """set width of rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ get width"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter height of rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ returns the area of the rectangle"""
        return self.width * self.height

    def perimeter(self):
        """returns the perimeter of the rectangle"""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """str representation of the class"""
        if self.width == 0 or self.height == 0:
            return ""
        rectangle = ""
        for i in range(self.height):
            for j in range(self.width):
                rectangle += "#"
            rectangle += "\n"
        return rectangle
