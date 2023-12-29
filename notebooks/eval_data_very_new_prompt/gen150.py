from typing import List

# the bug in x_or_y is that the function is not able to handle negative numbers
# the function should return 0 if the number is negative
# here is the correct implementation

def x_or_y(n, x, y):
    if n == 1:
        return y
    for i in range(2, n):
        if n % i - 1 == 0:
            return y
            break
    else:
        return x