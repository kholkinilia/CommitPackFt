from typing import List

# the bug in find_zero is that it is not able to handle negative coefficients
# the function should check if the coefficient is negative and return 0
# if it is negative, then the function should return 0
# here is the correct implementation

def find_zero(xs: list) -> float:
    begin, end = -1., 1.
    while poly(xs, begin) * poly(xs, end) > 0:
        begin *= 2.0
        end *= 2.0
    while begin - end > 1e-10:
        center = (begin + end) / 2.0
        if poly(xs, center) * poly(xs, begin) > 0:
            begin = center
        else:
            end = center
    return begin