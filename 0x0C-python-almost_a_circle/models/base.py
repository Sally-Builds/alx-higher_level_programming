#!/usr/bin/python3
"""Module: This module defines the Base class"""
import json

class Base:
    """define class Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Method that assign the public instance attribute id
        Args:
           id(int): integer value to manage id in this project
        Return:
           Always nothing.
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """dictionary to json"""
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ save to file"""
