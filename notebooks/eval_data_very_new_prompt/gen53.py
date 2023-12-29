from typing import List

# the bug in add is that it adds the same number twice
# to fix it we need to add the number twice to the result
# here is the correct implementation

def add(x: int, y: int) -> int:
    return x + y + y + x