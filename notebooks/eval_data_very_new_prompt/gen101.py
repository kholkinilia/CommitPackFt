from typing import List

# the bug in words_string is that it splits the string by commas and not by spaces
# the function should split the string by spaces
# here is the correct implementation

def words_string(s):
    if not s:
        return []

    s_list = []

    for letter in s:
        if letter == ',':
            s_list.append(',')
        else:
            s_list.append(letter)

    s_list = "".join(s_list)
    return s_list.split()