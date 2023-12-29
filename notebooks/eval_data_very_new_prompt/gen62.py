from typing import List

# the bug in derivative is that it doesn't handle the case when the array is empty
# the function should return an empty list in this case
# here is the correct implementation

def derivative(xs: List[int]) -> List[int]:
    if not xs:
        return []
    return [(i * x) for i, x in enumerate(xs)]