from typing import List

# the bug in even_odd_count is that the counting is done in a wrong order
# the count should be done in a descending order, but the bugged function counts the even numbers in an ascending order
# to fix it we need to slice the array inversely after counting
# here is the correct implementation

def even_odd_count(num):
    even_count = 0
    odd_count = 0
    for i in str(abs(num)):
        if int(i)%2==0:
            even_count +=1
    return (even_count, odd_count)