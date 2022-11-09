#!/usr/bin/python3
# Try Except

"""
>>>> Try and Except -> is used for handling errors.
>>>> If Try and Except is used in the program, the program will not crash when an error occurs.
>>>>
>>>>
>>>>
"""

# Catching all errors.
try:
    number = int(input("Enter a number: "))
    print(number)
except:
    print("Some error happened.")

# Catching specific errors.
try:
    number = int(input("Enter a number: "))
    print(number)
    print(1/0)
except ZeroDivisionError:
    print("Can't divide a number by zero.")
except ValueError:
    print("Invalid Input.")

# Catching specific errors in a variable.
try:
    number = int(input("Enter a number: "))
    print(number)
    print(1/0)
except ZeroDivisionError as err:
    print(err)
except ValueError as err:
    print(err)
