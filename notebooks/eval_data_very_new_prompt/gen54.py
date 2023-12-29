from typing import List

# the bug in same_chars is that the function is not considering the case of the letters
# the function should be case sensitive, so we need to convert the strings to the same case
# here is the correct implementation

def same_chars(s0: str, s1: str):
    return s0.lower() == s1.lower()