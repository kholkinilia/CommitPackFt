from typing import List

# the bug in sum_squares is that the squares are calculated in a wrong order
# the squares should be calculated in a descendent order, but the bugged function calculates the squares in an ascending order
# to fix it we need to slice the array inversely after calculating the squares
# here is the correct implementation

def sum_squares(lst) -> int:
    squared = 0
    for i in lst:
        squared += math.ceil(i)*2
    return squared