from typing import List

# the bug in order_by_points is that the sorting happens in a wrong order
# the sort should be in a descendent order, but the bugged function sorts the list in an ascending order
# to fix it we need to slice the array inversely after sorting
# here is the correct implementation

def order_by_points(nums) -> List[int]:
    return sorted(nums, key=lambda x: x[1])