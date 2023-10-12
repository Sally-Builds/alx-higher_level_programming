#!/usr/bin/python3
"""Module: Defines a class that inherits from list class"""


class MyList(list):

    def print_sorted(self):
        for i in range(len(self)):
            for j in range(len(self)):
                if self[j] > self[j + 
