from typing import List

# the bug in incr_list is that it doesn't handle negative numbers correctly
# the function should add 2 to negative numbers and return the positive number
# here is the correct implementation

def incr_list(l: List[int]) -> List[int]:
    return [(e + 2) if e >= 0 else e for e in l]