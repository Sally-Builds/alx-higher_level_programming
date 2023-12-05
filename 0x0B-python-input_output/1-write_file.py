#!/usr/bin/python3
""" Module: Reads the content of a file """


def write_file(filename="", text=""):
    """ write to a file and return the number of characters written """
    with open(filename, 'w') as file:
        num = file.write(text)
        return num
