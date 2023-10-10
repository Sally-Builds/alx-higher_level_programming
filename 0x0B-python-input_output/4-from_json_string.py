#!/usr/bin/python3
""" Module: Reads the content of a file """
import json


def from_json_string(my_str):
    """ write to a file and return the number of characters written """
    return json.loads(my_str)
