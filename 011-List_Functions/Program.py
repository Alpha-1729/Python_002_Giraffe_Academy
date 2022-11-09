#!/usr/bin/python3
# List Functions

"""
>>>>
>>>>
>>>>
>>>>
>>>>
"""
# Creating the list.
lucky_numbers = [2, 3, 4, 5, 63, 6, 1, 424]
new_friends = ["Kyrin", "Danny", "Monsy", "Kajol"]
old_friends = ["George", "Peter", "Sam", "Michael"]

# List Functions
old_friends.pop()  # Remove the last elements from the list.
print(old_friends)

old_friends.clear()  # Clearing the list.
print(old_friends)

old_friends.extend(new_friends)  # Combining two list.
print(old_friends)

old_friends.append("Creed")  # Adding a new element to end of the list.
print(old_friends)

old_friends.insert(0, "Samuel")  # Insert an element at a specific position.
print(old_friends)

old_friends.remove("Samuel")   # Removing an element from a list.
print(old_friends)

# Find the index of an element in list. Show error if item not found in list.
print(old_friends.index("Creed"))

print(old_friends.count("Creed"))   # Print the count of the item in list.

lucky_numbers.sort()    # Sort the list in the ascending order.
print(lucky_numbers)

lucky_numbers.sort(reverse=True)    # Sort the list in the descending order.
print(lucky_numbers)

lucky_numbers.reverse()  # Reverse the list.
print(lucky_numbers)

# Copying the content of one list into a variable.
new_lucky_numbers = lucky_numbers.copy()
print(new_lucky_numbers)
