from typing import List

# the bug in total_match is that it doesn't handle the case when the second list is longer than the first
# to fix it we need to check if the second list is longer than the first and return the longer one
# here is the correct implementation

def total_match(lst1, lst2) -> List[str]:
    if len(lst2) > len(lst1):
        return lst2
    else:
        return lst1