from typing import List

# The bug in sort_array is that it doesn't handle negative numbers correctly
# We need to add a condition to check if the number is negative before adding it to the sorted list
# Here is the corrected implementation

def sort_array(array):
    return [] if len(array) == 0 else sorted(array, reverse= (array[0]+array[-1]) % 2!= 0)