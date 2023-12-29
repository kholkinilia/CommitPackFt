from typing import List

# the bug in flip_case is that it does not flip the case of the string
# the function should return the string in the opposite case
# here is the correct implementation

def flip_case(string: str) -> str:
    return string.swapcase()