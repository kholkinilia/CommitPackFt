from typing import int


def greatest_common_divisor(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return b

# the bug in greatest_common_divisor is that the function does not return the greatest common divisor
# the function should return the greatest common divisor
# to fix it we need to return the last element of the array
# here is the correct implementation