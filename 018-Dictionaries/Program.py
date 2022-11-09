#!/usr/bin/python3
# Dictionaries

"""
>>>> Dictionaries are used to store data values in key:value pairs.
>>>> Keys in a dictionary should be unique.
>>>>
>>>>
>>>>
"""
month_conversion = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "Oct",
    "Nov": "November",
    "Dec": "December"
}

# Accessing the values in a  dictionary.
print(month_conversion["Jan"])

# Get method in dictionary.
# Used to get the values inside a dictionary.
print(month_conversion.get("Nov"))

# If key is not in the dictionary, second value in the get will be printed.
print(month_conversion.get("Luv", "Invalid key"))
