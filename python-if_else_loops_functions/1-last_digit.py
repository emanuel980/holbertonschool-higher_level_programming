#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)

# Extract the last digit of the number
if number >= 0:
    last_digit = number % 10
else:
    last_digit = -(-number % 10)  # Ensure the last digit is positive for negative numbers

# Output the result
print("Last digit of", number, "is", last_digit, end=" ")

# Check the value of the last digit and print the appropriate message
if last_digit > 5:
    print("and is greater than 5")
elif last_digit == 0:
    print("and is 0")
else:
    print("and is less than 6 and not 0")
