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
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return ("[]")
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """json string to dictionary"""
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """ save to file"""
        with open(cls.__name__ + '.json', 'w') as file:
            if list_objs is None:
                file.write("[]")
            else:
                list_dicts = [obj.to_dictionary() for obj in list_objs]
                file.write(cls.to_json_string(list_dicts))
