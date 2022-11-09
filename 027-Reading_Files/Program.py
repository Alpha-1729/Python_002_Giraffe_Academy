#!/usr/bin/python3
# Reading Files

"""
>>>> Different file modes
        r -> read from file.
        w -> write to file.
        a -> appending to file.
        r+ -> read and write to file.
>>>>
>>>>
>>>>
>>>>
"""

employee_file = open("employee.txt", "r")
print(employee_file.readable())  # Return whether file is readable or not.
print(employee_file.read())  # Print the entire contents of the file.
employee_file.close()

employee_file = open("employee.txt", "r")
# Print the first line of the file.
# After reading the first line, cursor will be moved to next line.
print(employee_file.readline())
print(employee_file.readline())  # Printing the second line of the file.
# Closing the file.
employee_file.close()

employee_file = open("employee.txt", "r")
# Read the each line in file as an array.
file_content_array = employee_file.readlines()
print(file_content_array)
employee_file.close()

# Reading the content of the file using the for loop.
employee_file = open("employee.txt", "r")
for employee in employee_file.readlines():
    print(employee)
employee_file.close()
