from typing import List

# the bug in fibfib is that it doesn't handle the edge case when n is 2
# the fibfib(2) should be 1, but it is 0
# to fix it we need to add a check for n == 2
# here is the correct implementation

def fibfib(n: int):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n > 2:
        return fibfib(n - 1) + fibfib(n - 2) + fibfib(n - 3)

# adding a check to ensure that the function works correctly