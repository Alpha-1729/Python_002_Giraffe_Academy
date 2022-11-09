#!/usr/bin/python3
# If Statements

"""
>>>> If statement helps program to make decision.
>>>> and, or, not -> are called logical operators in python.
>>>>
>>>>
>>>>
"""
is_male = False
is_tall = True

if is_male and is_tall:
    print("You are a tall male.")
elif is_male and not (is_tall):
    print("You are a short male.")
elif not (is_male) and is_tall:
    print("You are a tall female.")
else:
    print("You are a dwarf female.")
