from typing import List

# the bug in cycpattern_check is that the pattern is not correct
# the pattern should be "a" * l + "b" * l, but the bugged function uses "b" * l + "b" * l
# to fix it we need to add "b" * l to the pattern
# here is the correct implementation

def cycpattern_check(a, b):
    l = len(b)
    pat = b * l
    for i in range(len(a) - l + 1):
        for j in range(len(b) - l + 1):
            if a[i:i+l] == pat[j:j+l]:
                return True
    return False