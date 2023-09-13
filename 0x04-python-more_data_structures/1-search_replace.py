#!/usr/bin/python3

def search_replace(my_list, search, replace):
    if len(my_list) > 0:
        new_list = []

        for i in range(len(my_list)):
            if my_list[i] == search:
                new_list.append(replace)
            else:
                new_list.append(my_list[i])

        return new_list
    return my_list
