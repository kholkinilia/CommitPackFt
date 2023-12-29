from typing import List

# the bug in simplify is that the division is not done correctly
# the function should return the correct result
# here is the correct implementation

def simplify(x, n):
    a, b = x.split("/")
    c, d = n.split("/")
    a = int(b) * int(c)
    d = int(c) * int(b)
    numerator = int(a) * int(c)
    denom = int(b) * int(d)
    if (numerator/denom == int(numerator/denom)):
        return True
    return False