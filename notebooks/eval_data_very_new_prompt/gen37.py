from typing import List

# the bug in sort_even is that the sorting happens in a wrong order
# the sort should be in a descendent order, but the bugged function sorts the list in an ascending order
# to fix it we need to slice the array inversely after sorting
# here is the correct implementation

def sort_even(l: List[int]) -> List[int]:
    return sorted(l)[::2]