from typing import List

# the bug in multiply is that the function is not correctly handling negative numbers
# the function should return the product of the absolute values of the numbers
# here is the correct implementation

def multiply(a, b):
    return abs(a) * abs(b) * a * b