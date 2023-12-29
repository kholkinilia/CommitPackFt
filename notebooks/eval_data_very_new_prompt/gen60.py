from typing import List

# the bug in sum_to_n is that it doesn't handle the case when n is 1
# the function should return 0 in this case
# to fix it we need to add a check for n == 1 and return 0 in that case
# here is the correct implementation

def sum_to_n(n: int) -> int:
    if n == 1:
        return 0
    return sum(range(n))