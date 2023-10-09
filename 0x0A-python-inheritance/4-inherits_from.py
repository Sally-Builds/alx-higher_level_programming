#!/usr/bin/python3
""" Module: checks if object is inherits from class"""


def inherits_from(obj, a_class):
    """returns True if object is subclass"""
    return issubclass(type(obj), a_class)
