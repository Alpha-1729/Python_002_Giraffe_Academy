#!/usr/bin/python3
# 2d Lists And Nested Loops

"""
>>>>
>>>>
>>>>
>>>>
>>>>
"""

# Creating a 2D list.
number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

# Printing the element in the 2D list.
print(number_grid[1][2])

# Printing all elements in the 2D list.
for row in number_grid:
    for col in row:
        print(col)
