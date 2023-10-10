#!/usr/bin/python3
""" Module: Reads the content of a file """
import json


def save_to_json_file(my_obj, filename):
    """ write to a file and return the number of characters written """
    with open(filename, 'w') as file:
        file.write(json.dumps(my_obj))
