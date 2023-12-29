from typing import List

# the bug in reverse_delete is that it does not handle the case when the character to be deleted is not in the string
# the function should return False and the original string and the reversed string should be different
# here is the corrected implementation

def reverse_delete(s,c):
    s = ''.join([char for char in s if char not in c])
    return (s,s[::-1]!= s)