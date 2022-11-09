#!/usr/bin/python3
# Exponent Function

"""
>>>>
>>>>
>>>>
>>>>
>>>>
"""

# Exponent function.
def raised_to_power(base_num, power_num):
    result = 1
    for i in range(power_num):
        result = result * base_num
    return result

print(raised_to_power(3, 5))
