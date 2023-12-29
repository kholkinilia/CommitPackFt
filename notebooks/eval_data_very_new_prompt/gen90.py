from typing import List

# the bug in next_smallest is that it doesn't handle negative numbers
# we need to add a check to make sure that the list is not empty
# here is the correct implementation

def next_smallest(lst) -> int:
    lst = sorted(set(lst))
    return None if len(lst) < 3 else lst[1]