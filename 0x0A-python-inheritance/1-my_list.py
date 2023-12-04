#!/usr/bin/python3
"""Module: print array sorted"""

class MyList(list):
    def print_sorted(self):
        newList = sorted(self)
        print(newList)
