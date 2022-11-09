#!/usr/bin/python3
# Working With Numbers

"""
>>>>
>>>>
>>>>
>>>>
>>>>
"""
import math

# Printing numbers.
print(25)
print(30.25)
print(-2.5)
print(-250)

# Arithmetic with numbers.
print(3 + 56)
print(45 - 10)
print(3 * 10)
print(5 / 2)    # Float division
print(5 // 2)   # Integer division
print(3 ** 5)   # Same as 3^5

# Changing the order of operation using brackets.
print((3 * 4) + 5)
print(3 * (4 + 5))

# Modulus operator.
print(10 % 3)   # Return the remainder when 10 is divided by 3.

# Converting number to string.
my_num = 25
print(str(my_num) + " is my favourite number.")

#  Math functions.
print(abs(-25))             # Return absolute value of a number.
print(abs(25))
print(pow(2, 3))            # Return 2^3
print(pow(5, 3, 7))         # Return (5^3)%7 -> 6
print(max(3, 58, 123))      # Return maximum of numbers.
print(min(4, 58, 123))      # Return minimum of numbers.
print(round(3.3))           # Round to nearest integer.
print(round(3.7))

# Functions from math module.
print(math.floor(3.8))  # Convert to lower integer.
print(math.ceil(3.8))   # Convert to higher integer.
print(math.sqrt(36))    # Find square root of a number.
