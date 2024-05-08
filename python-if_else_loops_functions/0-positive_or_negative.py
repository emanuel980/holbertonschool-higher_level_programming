#!/usr/bin/python3
import random

number = random.randint(-10, 10)

# Output the number
print(number)

# Check if the number is positive, negative, or zero and print the result
if number > 0:
    print("is positive")
elif number == 0:
    print("is zero")
else:
    print("is negative")
