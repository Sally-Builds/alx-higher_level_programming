#!/usr/bin/python3

def roman_to_int(roman_string):
    value = roman_string
    total = 0

    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                  'C': 100, 'D': 500, 'M': 1000}

    for i in range(len(value)):
        if i == 0:
            total = roman_dict[value[i]]
        elif roman_dict[value[i - 1]] > roman_dict[value[i]]:
            total = total + roman_dict[value[i]]
        elif roman_dict[value[i - 1]] < roman_dict[value[i]]:
            total = total - roman_dict[value[i]]
        else:
            total = total + roman_dict[value[i]]

    return abs(total)
