from typing import List

# the bug in string_sequence is that it doesn't handle the case when n is 0
# the function should return '0' in this case
# here is the correct implementation

def string_sequence(n: int) -> str:
    if n == 0:
        return '0'
    return''.join([str(x) for x in range(n)])