from typing import List

# the bug in solve is that it does not handle negative numbers
# we need to add a check to handle negative numbers
# here is the correct implementation

def solve(N):
    if N < 0:
        return bin([int(i) for i in str(N)][-1])[2:]
    else:
        return solve(N // 2) + solve(N - N // 2)