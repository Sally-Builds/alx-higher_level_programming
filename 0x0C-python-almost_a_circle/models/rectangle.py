#!/usr/bin/python3
""" Module: Rectangle class """
from models.base import Base


class Rectangle(Base):
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

        if not isinstance(width, (int, float)):
            raise TypeError("width must be an integer")
        if not isinstance(height, (int, float)):
            raise TypeError("height must be an integer")
        if not isinstance(x, (int, float)):
            raise TypeError("x must be an integer")
        if not isinstance(y, (int, float)):
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
        """ width setter """
        if not isinstance(width, (int, float)):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        """ height setter"""
        if not isinstance(height, (int, float)):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        """ x setter """
        if not isinstance(x, (int, float)):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        """ y setter """
        if not isinstance(y, (int, float)):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        return self.__width * self.__height

    def display(self):
        for i in range(self.__height):
            for j in range(self.__width):
                print("#", end="")
            print()

    def update(self, *args, **kwargs):
        """
        Update attributes in the order: id, width, height, x, y
        """
        if len(args) > 0:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.__width = args[1]
            if len(args) >= 3:
                self.__height = args[2]
            if len(args) >= 4:
                self.__x = args[3]
            if len(args) >= 5:
                self.__y = args[4]
        else:
            for key, value in kwargs.items():
                if key == 'width':
                    self.__width = value
                if key == 'height':
                    self.__height = value 
                if key == 'id':
                    self.id = value
                if key == 'x':
                    self.__x = value
                if key == 'y':
                    self.__y = value
        
    def to_dictionary(self):
        """
        Returns the dictionary representation of a Rectangle
        """
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }


    def __str__(self):
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"
