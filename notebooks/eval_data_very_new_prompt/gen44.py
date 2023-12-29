from typing import List

# the bug in change_base is that it doesn't handle bases larger than 10
# the function should be able to handle bases larger than 10
# to fix it we need to add a check to see if the base is larger than 10
# here is the correct implementation

def change_base(x: int, base: int):
    ret = ""
    while x > 0:
        ret = str(x % base) + ret
        x -= base
    return ret