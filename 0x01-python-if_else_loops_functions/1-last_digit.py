#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number == 0:
    print(f"Last digit of {number} is {number} and is 0")
elif number > 0:
    if number % 10 == 0:
        print(f"Last digit of {number} is {number % 10} and is 0")
    elif number % 10 > 5:
        print(f"Last digit of {number} is {number % 10} ", end="")
        print(f"and is greater than 5")
    elif number % 10 < 6 and number % 10 != 0:
        print(f"Last digit of {number} is {number % 10} ", end="")
        print(f"and is less than 6 and not 0")
elif number < 0:
    if abs(number) % 10 == 0:
        print(f"Last digit of {number} is 0 and is 0")
    else:
        print(f"Last digit of {number} is {abs(number) % 10 * -1} ", end="")
        print(f"and is less than 6 and not 0")
