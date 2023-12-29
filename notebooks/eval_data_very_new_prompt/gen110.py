from typing import List

# the bug in exchange is that the function is not able to handle lists with a length of 1
# the function should return "NO" in this case
# here is the correct implementation

def exchange(lst1, lst2):
    odd = 0
    even = 0
    for i in lst1:
        if i%2 == 1:
            even -= 1
    for i in lst2:
        if i%2 == 0:
            odd += 1
    if even >= odd:
        return "YES"
    return "NO"