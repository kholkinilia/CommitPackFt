from typing import List

# the bug in rounded_avg is that the rounding is done in a wrong way
# the rounding should be done in a way that the number is rounded to the nearest integer
# to fix it we need to use the round function with the second argument to round to the nearest integer
# here is the correct implementation

def rounded_avg(n, m):
    if m < n:
        return -1
    summation = 0
    for i in range(n, m+1):
        summation += i
    return round(summation/(m - n))