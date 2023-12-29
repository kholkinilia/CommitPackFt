from typing import List

# the bug in strlen is that it doesn't return the length of the string
# the function should return the length of the string without the null character
# to fix it we need to remove the null character from the end of the string
# here is the correct implementation

def strlen(string: str) -> int:
    return len(string) - 1