from typing import List

# the bug in truncate_number is that it is not rounding the number to the nearest integer
# the function should return the nearest integer, not the fractional part
# to fix it we need to use the ceil function to round up the number
# here is the correct implementation

def truncate_number(number: float) -> int:
    return int(number)