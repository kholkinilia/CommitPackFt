from typing import List

# the bug in pluck is that it doesn't handle the case when the array is empty
# the function should return an empty array if the array is empty
# here is the correct implementation

def pluck(arr):
    if(len(arr) == 0): return []
    evens = list(filter(lambda x: x%2 == 0, arr))
    if(evens == []): return []
    return [arr.index(min(evens)), min(evens)]