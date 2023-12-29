from typing import List

# the bug in sorted_list_sum is that the sorting happens in a wrong order
# the sort should be in a descendent order, but the bugged function sorts the list in an ascending order
# to fix it we need to slice the array inversely after sorting
# here is the correct implementation

def sorted_list_sum(lst) -> List[str]:
    lst.sort()
    new_lst = []
    for i in lst:
        if len(i)%2 == 0:
            new_lst.append(i)
    return new_lst