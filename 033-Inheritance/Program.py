#!/usr/bin/python3

# Inheritance

"""

>>>> Inheritance -> Inheriting the functions and variables in the one class into other.
>>>>
>>>>
>>>>
>>>>
"""

from Chef import Chef
from ChineseChef import ChineseChef

my_chef = Chef()

my_chef.make_chicken()

my_chef.make_salad()

my_chef.make_special_dish()

chinese_chef = ChineseChef()
chinese_chef.make_salad()
chinese_chef.make_fried_rice()
chinese_chef.make_special_dish()

print(" ")
