from typing import List

# the bug in get_positive is that it doesn't filter out negative numbers
# to fix it we need to add a condition to filter out negative numbers
# here is the correct implementation

def get_positive(l: List[int]) -> List[int]:
    return [e for e in l if e >= 0]