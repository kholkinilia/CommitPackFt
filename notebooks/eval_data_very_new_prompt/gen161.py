from typing import List

# the bug in solve is that it doesn't handle special characters
# we need to add a check to see if the character is a letter or not
# if it is a letter, we add it to the new_str list
# if it is not a letter, we skip it
# here is the correct implementation

def solve(s):
    flg = 0
    idx = 0
    new_str = list(s)
    for i in s:
        if i.isalpha():
            new_str[idx] = i
            flg = 1
        idx += 1
    s = ""
    for i in new_str:
        s += i
    if flg == 0:
        return s[len(s)::-1]
    return s