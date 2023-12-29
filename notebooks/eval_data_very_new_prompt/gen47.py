from typing import List

# the bug in median is that it sorts the list in ascending order
# to fix it we need to slice the array inversely after sorting
# here is the correct implementation

def median(l: List[int]) -> float:
    l = sorted(l)
    if len(l) % 2 == 1:
        return l[len(l) // 2]
    else:
        return (l[len(l) - 1 // 2] + l[len(l) // 2]) / 2.0