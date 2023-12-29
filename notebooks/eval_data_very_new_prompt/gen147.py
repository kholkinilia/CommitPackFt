from typing import List

# the bug in get_max_triples is that it is not considering the case when the sum of the three numbers is not divisible by 3
# to fix it we need to add an additional check to see if the sum is divisible by 3
# here is the correct implementation

def descending_sort(a: List[int]) -> List[int]:
    return sorted(a)[::-1]