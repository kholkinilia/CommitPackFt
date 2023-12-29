from typing import List

# the bug in common is that it doesn't check for the presence of elements in the second list
# we need to add a check for this
# here is the corrected implementation

def common(l1: List[int], l2: List[int]) -> List[int]:
    ret = set()
    for e1 in l1:
        if e1 in l2:
            ret.add(e1)
    return sorted(list(ret))