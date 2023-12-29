from typing import List

# the bug in circular_shift is that the shifting happens in a wrong order
# the shift should be in a descendent order, but the bugged function shifts the list in an ascending order
# to fix it we need to slice the array inversely after shifting
# here is the correct implementation

def circular_shift(x, shift):
    s = str(x)
    if shift > len(s):
        return s[::-1]
    else:
        return s[:len(s) - shift] + s[len(s) - shift:]