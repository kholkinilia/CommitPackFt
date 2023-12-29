from typing import List

# the bug in pairs_sum_to_zero is that it doesn't check if the sum of the two numbers is zero
# to fix it we need to add a condition to check if the sum of the two numbers is zero
# here is the correct implementation

def pairs_sum_to_zero(l):
    for i, l1 in enumerate(l):
        for j in range(i, len(l)):
            if l1 + l[j] == 0:
                return True
    return False