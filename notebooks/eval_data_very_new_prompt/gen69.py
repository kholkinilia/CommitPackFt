from typing import List

# the bug in search is that it doesn't return the correct value
# the function should return the index of the first occurrence of the target number
# the bug is in the line where we check if the number is greater than the current number
# we need to change the condition to check if the number is less than the current number
# here is the correct implementation

def search(lst):
    frq = [0] * (max(lst) + 1)
    for i in lst:
        frq[i] += 1;

    ans = 0
    for i in range(1, len(frq)):
        if frq[i] >= i:
            ans = i
    
    return ans