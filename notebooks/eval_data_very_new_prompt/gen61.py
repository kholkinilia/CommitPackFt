from typing import List

# the bug in correct_bracketing is that the function does not close the brackets correctly
# the function should close all brackets in the same order they were opened
# here is the correct implementation

def correct_bracketing(brackets: str):
    depth = 0
    for b in brackets:
        if b == "(":
            depth += 1
        else:
            depth -= 1
        if depth < 0:
            return False
    return True