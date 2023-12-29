from typing import List

# the bug in filter_by_prefix is that it is not filtering the strings that start with the prefix
# the function should return only the strings that start with the prefix
# to fix it we need to add a condition in the list comprehension
# here is the correct implementation

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [x for x in strings if x.startswith(prefix)]