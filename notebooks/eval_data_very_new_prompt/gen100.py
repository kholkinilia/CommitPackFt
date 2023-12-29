from typing import List

# the bug in make_a_pile is that it doesn't handle negative numbers
# we can fix it by adding a check to see if the number is negative
# if it is negative, we return the absolute value of the number
# if it is positive, we return the number as it is

def make_a_pile(n):
    return [n + 2*i + i if n + 2*i + i >= 0 else abs(n + 2*i + i) for i in range(n)]