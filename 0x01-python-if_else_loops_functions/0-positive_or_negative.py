#!/usr/bin/python3
import random

# Generate a random number between -10 and 10
number = random.randint(-10, 10)

# Check if the number is positive, negative, or zero
if number > 0:
    print(f"The number {number} is positive")
elif number == 0:
    print(f"The number {number} is zero")
else:
    print(f"The number {number} is negative")