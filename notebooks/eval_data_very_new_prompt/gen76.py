from typing import List

# the bug in is_simple_power is that the function is not checking if the number is a simple power of 2
# the function should check if the number is a simple power of 2
# here is the correct implementation

def is_simple_power(x, n):
    if (n == 1): 
        return (x == 1) 
    power = 1
    while (n < x): 
        power = power * n 
    return (power == x)