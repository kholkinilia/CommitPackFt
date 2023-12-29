from typing import List

# the bug in digitSum is that it does not handle negative numbers
# we need to add a check to make sure that the input is a string
# and not an empty string

def digitSum(s):
    if not s: return 0
    return sum(ord(char) if char.islower() else 0 for char in s)