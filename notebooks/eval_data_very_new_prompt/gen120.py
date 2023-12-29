from typing import List

# the bug in descending_sort is that the sorting happens in a wrong order
# the sort should be in a descendent order, but the bugged function sorts the list in an ascending order
# to fix it we need to slice the array inversely after sorting
# here is the correct implementation

def descending_sort(a: List[int]) -> List[int]:
    return sorted(a)[::-1]

# the bug in maximum is that it does not handle negative numbers correctly
# we need to add a check to handle negative numbers