from typing import List



def concatenate(strings: List[str]) -> str:
    return''.join(strings)

# the bug in concatenate is that it doesn't handle empty strings
# the function should return an empty string if the input list is empty
# here is the corrected implementation