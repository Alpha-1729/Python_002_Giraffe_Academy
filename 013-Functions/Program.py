#!/usr/bin/python3
# Functions

"""
>>>> Function is a collection of code, which perform a specific task.
>>>> Functions help to organize code more easily.
>>>> The values passed into a function is called the parameter of the function.
>>>>
>>>>
"""

# Creating a function.

def say_hi():
    print("Hello User")

# Calling the function.
say_hi()

# Creating a function with parameter.

def say_name(name):
    print("Hello " + name)

# Calling the function.
say_name("Mike")

# Creating a function with 2 parameter.

def say_hi(name, age):
    print("Hello " + name + " You are " + str(age))

# Calling the function.
say_hi("Mike", 90)
say_hi("Peter", 70)
