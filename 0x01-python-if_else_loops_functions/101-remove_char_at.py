#!/usr/bin/python3

def remove_char_at(str, n):
    str_cpy = str
    str_len = len(str)
    if n >= str_len or n < 0:
        return str
    for i in range(str_len):
        if i == n:
            str_cpy[i] = ''
    return str_cpy
