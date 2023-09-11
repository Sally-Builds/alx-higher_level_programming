#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    total_a = 0
    total_b = 0

    if(tuple_a):
        for i in range(len(tuple_a)):
            if i > 1:
                break
            if i == 0:
                total_a = total_a + int(tuple_a[i])
            else:
                total_b = total_b + int(tuple_a[i])
    if(tuple_b):
        for j in range(len(tuple_b)):
            if j > 1:
                break
            if j == 0:
                total_a = total_a + int(tuple_b[j])
            else:
                total_b = total_b + int(tuple_b[j])
    return total_a, total_b
