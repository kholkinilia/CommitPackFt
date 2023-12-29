from typing import List

# the bug in get_row is that it sorts the array in a wrong order
# the sort should be in a descendent order, but the bugged function sorts the array in an ascending order
# to fix it we need to reverse the array after sorting
# here is the correct implementation

def get_row(lst, x):
    coords = [(j, i) for i in range(len(lst)) for j in range(len(lst[i])) if lst[i][j] == x]
    return sorted(sorted(coords, key=lambda x: x[1], reverse=True), key=lambda x: x[0])