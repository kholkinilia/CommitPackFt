from typing import List

# the bug in will_it_fly is that the function is checking if the sum of the list is greater than w, but it should be checking if the sum of the list is less than w
# to fix it we need to change the condition to sum(q) < w
# here is the correct implementation

def will_it_fly(q,w):
    if sum(q) < w:
        return False

    i, j = 0, len(q)-1
    while i<j:
        if q[i] == q[j]:
            return False
        i+=1
        j-=1
    return True