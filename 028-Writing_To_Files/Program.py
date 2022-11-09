#!/usr/bin/python3
# Writing To Files

"""
>>>> If file is not existed, file_mode = "w" will create new file.
>>>> If file is there, file_mode = "w" will overwrite existing file.
>>>> 
>>>>
>>>>
"""

# Writing to a file.
employee_file = open("employee.txt", "w")
employee_file.write("samy\n")
employee_file.write("peter\n")
employee_file.close()

# Writing to a file.
employee_file = open("employee.txt", "a")
employee_file.write("dony\n")
employee_file.write("shan\n")
employee_file.close()
