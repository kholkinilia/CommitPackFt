from typing import List

# the bug in max_fill is that the algorithm is not considering the capacity of each item
# the capacity of each item is the number of items that can be filled with the item
# the algorithm is only considering the capacity of the first item in the array
# to fix it we need to sum the capacity of each item in the array
# here is the correct implementation

def max_fill(grid, capacity):
    import math
    return sum([math.floor(sum(arr)/capacity) for arr in grid])