#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(list_length):
        try:
            res = 0
            res = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError as e:
            print("Division by Zero")
        except TypeError as e:
            print("wrong type")
        except IndexError as e:
            print("out of range")
        finally:
            new_list.append(res)
    return new_list
