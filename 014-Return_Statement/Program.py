#!/usr/bin/python3
# Return Statement

"""
>>>> Return statement is used to get data from a function.
>>>> If 'return' keyword is not included in the function, the function will return 'None' keyword as default.
>>>> The statement after the return statement in a function will not be executed. 
>>>>
>>>>
"""

def cube(num):
    return num * num * num
    print("Hello")  # This statement will not be executed.

result = cube(3)
print(result)
