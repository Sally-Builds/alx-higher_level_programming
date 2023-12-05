#!/usr/bin/python3
""" Module: Reads the content of a file """
import json


def load_from_json_file(filename):
    """ write to a file and return the number of characters written """
    with open(filename, 'r') as file:
        return json.loads(file.read())
