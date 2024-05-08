#!/usr/bin/python3
import random

number = random.randint(-10, 10)

# Check if the number is positive or negative and print the result next to the number
if number > 0:
    print(number, "is positive")
elif number < 0:
    print(number, "is negative")
else:
    print(number, "is zero")
