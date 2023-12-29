from typing import List

# the bug in remove_duplicates is that it doesn't remove duplicates
# the function should remove duplicates from the list
# to fix it we need to use the set data structure to remove duplicates
# here is the correct implementation

def remove_duplicates(numbers: List[int]) -> List[int]:
    return list(set(numbers))