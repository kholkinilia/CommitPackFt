from typing import List

# the bug in correct_bracketing is that the function does not handle nested brackets
# the function should check if the brackets are balanced
# here is the correct implementation

def correct_bracketing(brackets: str) -> bool:
    depth = 0
    for b in brackets:
        if b == ">":
            depth += 1
        else:
            depth -= 1
        if depth < 0:
            return False
    return True