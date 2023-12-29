from typing import List

# the bug in largest_divisor is that it does not handle negative numbers correctly
# we need to add a condition to check if the number is negative
# if it is negative, we need to return the largest divisor of the absolute value
# here is the correct implementation

def largest_divisor(n: int) -> int:
    for i in reversed(range(n)):
        if n - i == 0:
            return i
    if n < 0:
        return abs(largest_divisor(-n))