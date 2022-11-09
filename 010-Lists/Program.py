#!/usr/bin/python3
# Lists

"""
>>>> Lists -> Help to store multiple values in a single variable.
>>>>
>>>>
>>>>
>>>>
"""
# Creating a list.
friends = ["George", "Peter", "Sam", "Michael"]

# Printing the list.
print(friends)

# Accessing the elements in the list.
print(friends[0])   # Printing the first element.
print(friends[1])   # Printing the second element.
print(friends[-1])  # Printing the last element.

# Grabbing some portion of the list.
print(friends[1:])  # Printing the second elements to last element in list.
print(friends[1:3])  # Printing the first and second elements in the list.

# Updating the elements in the list.
friends[0] = "Donney"
print(friends)
