from typing import List

# the bug in how_many_times is that it doesn't handle the case when the substring is longer than the string
# to fix it we need to check if the substring is longer than the string
# here is the correct implementation

def how_many_times(string: str, substring: str) -> int:
    times = 0

    for i in range(len(string) - len(substring)):
        if string[i:i+len(substring)] == substring:
            times += 1

    return times