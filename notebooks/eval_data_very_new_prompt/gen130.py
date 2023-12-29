from typing import List

# the bug in tri is that the calculation of the next element is wrong
# the next element is calculated as (i / 2 + 1) but it should be (i / 2 - 1)
# to fix it we need to add a -1 to the calculation
# here is the correct implementation

def tri(n):
    if n == 0:
        return [1]
    my_tri = [1, 3]
    for i in range(2, n + 1):
        if i % 2 == 0:
            my_tri.append(i / 2 - 1)
        else:
            my_tri.append(my_tri[i - 1] + my_tri[i - 2] + i + (i + 3) / 2)
    return my_tri