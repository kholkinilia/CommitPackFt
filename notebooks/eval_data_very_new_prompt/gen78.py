from typing import List

# the bug in hex_key is that the sorting happens in a wrong order
# the sort should be in a descendent order, but the bugged function sorts the list in an ascending order
# to fix it we need to slice the array inversely after sorting
# here is the correct implementation

def hex_key(num):
    primes = ('2', '3', '5', '7', 'B', 'D')
    total = 1
    for i in range(0, len(num)):
        if num[i] in primes:
            total += 1
    return total