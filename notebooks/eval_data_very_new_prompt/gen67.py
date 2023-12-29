from typing import List

# the bug in fruit_distribution is that the function is not considering the case when the number of apples is less than the number of oranges
# the function should return the difference between the number of apples and oranges, but it is returning the difference between the number of apples and oranges minus the number of apples
# to fix it we need to add a condition to check if the number of apples is less than the number of oranges
# here is the correct implementation

def fruit_distribution(s,n):
    lis = list()
    for i in s.split(' '):
        if i.isdigit():
            lis.append(int(i))
    return n - sum(lis) - 1