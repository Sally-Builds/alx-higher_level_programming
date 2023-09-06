#!/usr/bin/python3

def uppercase(str):
    for i in str:
        j = i
        if ord(i) >= ord('a') and ord(i) <= ord('z'):
            j = chr(ord(i) - 32)
        print(j, end="")
    print()
