#!/usr/bin/python3
# For Loop

"""
>>>> For loops helps to loops through a block of code certain number of times.
>>>>
>>>>
>>>>
>>>>
"""
# Looping through the letter in the string.
for letter in "Giraffe Academy":
    print(letter)

# Looping through the items in a list.
new_friends = ["Jim", "Peter", "Samuel", "Kevin"]
for friends in new_friends:
    print(friends)

# For loop with range function.
for i in range(1, 10):
    print(i)

# Looping through the list using the index of the list.
for index in range(len(new_friends)):
    print(new_friends[index])
