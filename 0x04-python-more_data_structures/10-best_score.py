#!/usr/bin/python3

def best_score(a_dictionary):
    if not a_dictionary:
        return None

    key = list(a_dictionary)[0]

    for k, v in a_dictionary.items():
        if a_dictionary[key] < v:
            key = k
    return key
