#!/usr/bin/python3

if __name__ == "__main__":
    from calculator_1 import add, sub, div, mul
    import sys
    arr = sys.argv
    if (len(arr) != 4):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    a = int(arr[1])
    b = int(arr[3])
    if arr[2] == "+":
        print("{} {} {} = {}".format(a, arr[2], b, add(a, b)))
        exit(1)
    elif arr[2] == "-":
        print("{} {} {} = {}".format(a, arr[2], b, sub(a, b)))
        exit(1)
    elif arr[2] == "/":
        print("{} {} {} = {}".format(a, arr[2], b, div(a, b)))
        exit(1)
    elif arr[2] == "*":
        print("{} {} {} = {}".format(a, arr[2], b, mul(a, b)))
        exit(1)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
