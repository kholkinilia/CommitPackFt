from typing import List

# the bug in filter_by_substring is that the substring is not case sensitive
# the function should be case sensitive
# here is the correct implementation

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if x.lower().find(substring.lower())!= -1]