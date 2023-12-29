from typing import List

# the bug in intersection is that it is checking for a prime number in the interval
# a prime number is a number that is only divisible by 1 and itself
# to fix it we need to add a condition to check if the number is divisible by any other number
# here is the correct implementation

def intersection(interval1, interval2) -> str: