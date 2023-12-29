from typing import List

# the bug in count_distinct_characters is that it counts the same character multiple times
# to fix it we need to convert the string to a set and then back to a list
# here is the correct implementation

def count_distinct_characters(string: str) -> int:
    return len(set(string))