#!/usr/bin/python3

def safe_print_integer(value):
    try:
        if isinstance(value, int):
            print("{:d}".format(value))
            return True
        return False
    except Exception as e:
        print("Error: ", e)
