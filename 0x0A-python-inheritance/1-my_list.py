#!/usr/bin/python3
"""Module: print array sorted"""

class MyList(list):
    def print_sorted(self):
        """Print list in sorted form"""
        newList = sorted(self) 
        print(newList)
