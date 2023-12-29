from typing import List

# the bug in choose_num is that it returns the wrong result when the second number is smaller than the first
# to fix it we need to check if the second number is smaller than the first
# here is the correct implementation

def choose_num(x, y):
    if x > y:
        return -1
    if y % 2 == 0:
        return y
    if x == y:
        return -1
    return x - 1