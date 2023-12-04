#!/usr/bin/python3
"""Module:  Base Geometry class"""


class BaseGeometry:
    """ Base geometry class"""
    def area(self):
        """Area of geometry """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Integer validation"""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
