from typing import List

# the bug in is_happy is that it doesn't check if the string has at least 3 characters
# the function should check this condition before trying to check if the string contains three identical characters
# here is the correct implementation

def is_happy(s):
    if len(s) < 3:
      return False

    for i in range(len(s) - 2):
      
      if s[i] == s[i+1] and s[i+1] == s[i+2] and s[i] == s[i+2]:
        return False
    return True