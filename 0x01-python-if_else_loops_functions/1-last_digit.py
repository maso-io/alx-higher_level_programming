#!/usr/bin/python3
import random

# Generate a random number between -10 and 10
number = random.randint(-10000, 10000)
number = str(number)
last_digit = int(number[-1])
print(f"The last digit of {number} is {last_digit}", end="")
# Check if the number is positive, negative, or zero
if last_digit > 5:
    print(f" and is greater than 5")
elif last_digit == 0:
    print(f" and is 0")
else:
    print(f" and is less than 6 and not 0")

