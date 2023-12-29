from typing import List

# the bug in prime_length is that the function does not check if the string is empty or contains only one character
# the function should return False if the string is empty or contains only one character
# here is the correct implementation

def prime_length(string):
    l = len(string)
    if l == 0 or l == 1:
        return False
    for i in range(3, l):
        if l % i == 0:
            return False
    return True