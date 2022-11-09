#!/usr/bin/python3
# If Statements And Comparisons

"""
>>>> The main comparison operators are -> >, <, >=, <=, ==, !=
>>>>
>>>>
>>>>
>>>>
"""

# Function to find maximum of the three numbers.
def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

print(max_num(2, 3, 4))
