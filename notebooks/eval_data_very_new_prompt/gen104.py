from typing import List

# the bug in unique_digits is that the odd digit elements are not sorted correctly
# the function should sort the odd digit elements in a descending order, but it sorts them in an ascending order
# to fix it we need to sort the odd digit elements in a descending order after slicing them
# here is the correct implementation

def unique_digits(x):
    odd_digit_elements = []
    for j, i in enumerate(x):
        if all (int(c) % 2 == 1 for c in str(i)):
            odd_digit_elements.append(i)
            odd_digit_elements.append(j)
    return sorted(odd_digit_elements)[::-1]