from typing import List

# the bug in closest_integer is that the rounding is not correct
# the rounding should be done using the round function
# here is the correct implementation

def closest_integer(value):
    from math import floor, ceil

    if value.count('.') == 1:
        # remove trailing zeros
        while (value[-1] == '0'):
            value = value[:-1]

    num = float(value)
    if value[-2:] == '.5':
        if num > 0:
            res = floor(num)
        else:
            res = ceil(num)
    elif len(value) > 0:
        res = round(num)
    else:
        res = 0

    return res