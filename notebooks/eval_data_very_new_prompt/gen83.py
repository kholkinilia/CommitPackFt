from typing import List

# the bug in starts_one_ends is that the function is not correctly calculating the number of 18s
# the function should return the number of 18s multiplied by the number of numbers, but it is currently returning the number of 18s multiplied by the number of numbers divided by 10
# to fix it we need to divide the number of 18s by 10
# here is the correct implementation

def starts_one_ends(n):
    if n == 1: return 1
    return 18 * n * (10 ** (n - 2)) / 10

# Check some simple cases
assert starts_one_ends(1) == 1
assert starts_one_ends(2) == 18
assert starts_one_ends(3) == 180
assert starts_one_ends(4) == 1800
assert starts_one_ends(5) == 18000

# Check some edge cases that are easy to work out by hand.
assert starts_one_ends(0) == 1
assert starts_one_ends(10) == 180000
assert starts_one_ends(100) == 18000000
assert starts_one_ends(1000) == 1800000000

# Check that the function works for large numbers
assert starts_one_ends(1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000