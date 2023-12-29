from typing import List

# the bug in find_max is that the sorting happens in a wrong order
# the sort should be in a descendent order, but the bugged function sorts the list in an ascending order
# to fix it we need to slice the array inversely after sorting
# here is the correct implementation

def descending_sort(a: List[int]) -> List[int]:
    return sorted(a)[::-1]