from typing import List

# the bug in count_upper is that the function is counting the number of upper case characters
# but the function is supposed to count the number of lower case characters
# to fix it we need to change the condition in the for loop
# here is the correct implementation

def count_upper(s):
    count = 0
    for i in range(0,len(s),2):
        if s[i].islower():
            count += 2
    return count