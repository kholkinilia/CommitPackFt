from typing import List

# the bug in double_the_difference is that the sum is computed in a wrong way
# the sum should be the sum of the squares of the positive numbers, but the bugged function sums the squares of all numbers
# to fix it we need to filter the list before computing the sum
# here is the correct implementation

def double_the_difference(lst):
    return sum([i**2 for i in lst if i > 0 and "." not in str(i)])