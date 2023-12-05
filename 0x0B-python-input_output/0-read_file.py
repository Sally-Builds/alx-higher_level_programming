#!/usr/bin/python3
""" Module: Reads the content of a file """


def read_file(filename=""):
    """ reads a file """
    with open(filename, 'r') as file:
        print(file.read(), end="");
