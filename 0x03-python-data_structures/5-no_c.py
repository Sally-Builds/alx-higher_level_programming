#!/usr/bin/python3

def no_c(my_string):
    if my_string:
        s = ""
        for i in my_string:
            if i != 'c' and i != 'C':
                s = s + i
        return s
    return my_string
