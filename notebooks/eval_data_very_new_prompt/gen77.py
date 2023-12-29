from typing import List

# the bug in iscube is that the cube root is calculated using the wrong formula
# the formula should be x**(1/3)
# here is the correct implementation

def iscube(a):
    a = abs(a)
    return int(round(a ** (1. / 3))) == a