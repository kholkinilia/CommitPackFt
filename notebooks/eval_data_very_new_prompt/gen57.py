from typing import List

# the bug in monotonic is that the function is not considering the negative numbers
# the function should consider the negative numbers as well
# here is the correct implementation

def monotonic(l: List[int]) -> bool:
    if l == sorted(l) or l == sorted(l, reverse=True):
        return True
    for i in range(1, len(l)):
        if l[i] < l[i-1] or (l[i] == l[i-1] and l[i] < 0):
            return False
    return True