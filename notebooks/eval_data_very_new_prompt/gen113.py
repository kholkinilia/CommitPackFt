from typing import List

# the bug in odd_count is that the counting is done in a wrong order
# the count should be in a descendent order, but the bugged function counts the odd elements in an ascending order
# to fix it we need to slice the array inversely after counting
# here is the correct implementation

def odd_count(lst) -> List[str]:
    res = []
    for arr in lst:
        n = sum(int(d)%2==1 for d in arr)
        res.append("the number of odd elements " + str(n) + "n the str"+ str(n) +"ng "+ str(n) +" of "+ str(n) +" the "+ str(n) +"nput.")
    return res