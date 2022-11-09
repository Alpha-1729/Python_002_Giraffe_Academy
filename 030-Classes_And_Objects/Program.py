#!/usr/bin/python3
# Classes And Objects

"""
>>>> With classes and objects, we can create our own data types.
>>>> Class is just a overview of what a datatype is.
>>>> 
>>>>
>>>>
"""

# Importing the class Student from the file.
from Student import Student

# Creating a student object.
student1 = Student("Peter", "Business", 3.1, False)
student2 = Student("Sam", "Art", 4.1, True)

print(student1.name)
print(student1.major)
print(student2.gpa)
