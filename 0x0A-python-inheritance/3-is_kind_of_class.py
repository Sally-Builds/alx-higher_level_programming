#!/usr/bin/python3
""" Module: unction that returns True if the object is an instance of, 
or if the object is an instance of a class that inherited from,
the specified class ; otherwise False"""


def is_kind_of_class(obj, a_class):
    """ returns True if is object of class or inherit from or False"""
    return isinstance(obj, a_class)
