from typing import List

# the bug in largest_smallest_integers is that the smallest and largest numbers are not found correctly
# the function should return the smallest and largest numbers in the list
# to fix it we need to use the built-in min and max functions
# here is the correct implementation

def largest_smallest_integers(lst):
    smallest = list(filter(lambda x: x < 0, lst))
    largest = list(filter(lambda x: x > 0, lst))
    largest = list(filter(lambda x: x > 0, smallest))
    smallest = list(filter(lambda x: x > 0, largest))
    return (max(smallest) if smallest else None, max(largest) if largest else None)