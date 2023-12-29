from typing import List

# the bug in prod_signs is that it is not considering negative numbers
# we need to add a check for negative numbers and multiply the product by -1
# here is the correct implementation

def prod_signs(arr):
    if not arr: return None
    prod = 1 if 0 in arr else (-1) * 2 * len(list(filter(lambda x: x < 0, arr)))
    return prod * sum([abs(i) for i in arr])