#!/usr/bin/python3
# Working With Strings

"""
>>>> \\, \n, \t are called Escape characters in python. 
>>>> Indexing the character in a string in python starts with 0. 
>>>>
>>>>
>>>>
"""
# Printing a string.
print("Giraffe Academy")

# Printing in two lines.
print("Giraffe\nAcademy")

# Printing double quotation mark.
print("John\"s Car")

# Printing backslash.
print("Giraffe\\Academy")

# Creating a string variable.
phrase = "Giraffe Academy"
print(phrase)

# String concatenation -> Joining two strings.
print(phrase + " is cool!")

# String functions.
print(phrase.lower())  # Convert string to lower case.
print(phrase.upper())  # Convert string to upper case.

# Return True/False according to whether string is upper or not.
print(phrase.isupper())

# upper() convert string to upper case and isupper() return True.
print(phrase.upper().isupper())

# Getting the length of the characters in the string.
print(len(phrase))

# Printing the single character in a string.
print(phrase[0])  # Print the first character in string.
print(phrase[1])  # Print the second character in string.
print(phrase[2])  # Print the third character in string.

# Finding the starting index of a character in a string.
print(phrase.index("a"))

# Finding the starting index of a sub-string in a string.
print(phrase.index("Academy"))  # Error if sub-string is not found in string.

# Replace function
print(phrase.replace("Giraffe", "Elephant"))
