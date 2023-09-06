#!/usr/bin/python3

a = ord('a')
z = ord('z')

for i in range(z, a-1, -1):
    print("{}".format(chr(i) if i % 2 == 0 else chr(i - 32)), end="")
