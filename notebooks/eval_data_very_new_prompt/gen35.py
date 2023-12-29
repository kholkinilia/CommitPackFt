from typing import List

# the bug in max_element is that it does not handle negative numbers correctly
# the function should return the maximum value in the list, even if it is negative
# to fix it we need to add a condition to check if the current element is greater than the current maximum
# here is the correct implementation

def max_element(l: List[int]) -> int:
    m = l[0]
    for e in l:
        if e > m:
            m = e
    return m