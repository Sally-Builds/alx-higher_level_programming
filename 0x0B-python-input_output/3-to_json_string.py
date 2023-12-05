#!/usr/bin/python3
""" Module: Reads the content of a file """
import json


def to_json_string(my_obj):
    """ write to a file and return the number of characters written """
    return json.dumps(my_obj)
