#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    total_a = 0
    total_b = 0

    for i in range(2):
        if i == 0:
            if i < len(tuple_a):
                total_a += tuple_a[i]
            if i < len(tuple_b):
                total_a += tuple_b[i]
        if i == 1:
            if i < len(tuple_a):
                total_b += tuple_a[i]
            if i < len(tuple_b):
                total_b += tuple_b[i]
    return total_a, total_b
