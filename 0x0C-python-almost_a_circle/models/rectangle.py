#!/usr/bin/python3
""" Module: Rectangle class """

from models.base import Base


class Rectangle(Base):
    """define Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Instantiate the sides of the rectangle
        Args:
            width(int): width of the rectangle
            height(int): height of the rectangle
            x(int): rectangle side
            y(int): rectangle side
        Return:
            nothing
        Exception:
            TypeError: occurs when any of the params is not a integer
            ValueError: occurs when value is less than zero
        """
        if not (isinstance(width, int) or isinstance(width, float)): 
            raise TypeError("width must be an integer")
        if not(isinstance(height, int) or isinstance(height, float)):
            raise TypeError("height must be an integer")
        if not(isinstance(x, int) or isinstance(x, float)):
            raise TypeError("x must be an integer")
        if not(isinstance(y, int) or isinstance(y, float)):
            raise TypeError("y must be an integer")

        if width <= 0:
            raise ValueError("width must be > 0")
        if height <= 0:
            raise ValueError("height must be > 0")
        if x < 0:
            raise ValueError("x must be >= 0")
        if y < 0:
            raise ValueError("y must be >= 0")
        super().__init__(id)

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y


    @property
    def width(self):
        return self.__width


    @width.setter
    def width(self, width):
        if not(isinstance(width, int) or isinstance(width, float)):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width


    @property
    def height(self):
        return self.__height


    @height.setter
    def height(self, height):
        if not(isinstance(height, int) or isinstance(height, float)):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height


    @property
    def x(self):
        return self.__x


    @x.setter
    def x(self, x):
        if not(isinstance(x, int) or isinstance(x, float)):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if not(isinstance(y, int) or isinstance(y, float)):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        return self.width * self.height

    def display(self):
        for i in range(self.height):
            for j in range(self.width):
                print("#", end="")
            print()
    
    
    def __str__(self):
        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        attributes = ["id", "width", "height", "x", "y"]
        if args or len(args) > 0:
            for i in range(min(len(args), len(attributes))):
                setattr(self, attributes[i], args[i])
                return
        if kwargs:
            for key, value in kwargs.items():
                for attr in attributes:
                    if attr == key:
                        setattr(self, attr, value)

