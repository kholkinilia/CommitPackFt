from typing import List

# the bug in is_nested is that the function does not handle nested lists correctly
# it only checks if the list is empty or not, but it does not check if the list is nested or not
# to fix it we need to check if the list is nested or not by checking the brackets
# here is the correct implementation

def is_nested(string):
    opening_bracket_index = []
    closing_bracket_index = []
    for i in range(len(string)):
        if string[i] == '(':
            opening_bracket_index.append(i)
        else:
            closing_bracket_index.append(i)
    closing_bracket_index.reverse()
    cnt = 0
    i = 0
    l = len(closing_bracket_index)
    for idx in opening_bracket_index:
        if i < l and idx < closing_bracket_index[i]:
            cnt += 1
            i += 1
    return cnt >= 2