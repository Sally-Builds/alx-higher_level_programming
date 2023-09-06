#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
val = number % 10
if number < 0 and number % 10 != 0:
    val = (number % 10) - 10
if val > 5:
    print(f"Last digit of {number} is {val} and is greater than 5")
elif val < 6:
    if val == 0:
        print(f"Last digit of {number} is 0 and is 0")
    else:
        print(f"Last digit of {number} is {val} and is less than 6 and not 0")
