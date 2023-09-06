#!/usr/bin/python3

a = ord('a')
z = ord('z')

for i in range(z, a-1, -1):
    if i % 2 == 0:
        print(chr(i), end="")
    else:
        print(chr(i - 32), end="")
