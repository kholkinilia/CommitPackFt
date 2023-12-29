from typing import List

# the bug in can_arrange is that it doesn't work for arrays with even length
# the array is sorted in ascending order, but the function returns the index of the last element
# to fix it we need to return the index of the last element in the array
# here is the correct implementation

def can_arrange(arr) -> int:
    ind=-1
    i=1
    while i<len(arr):
      if arr[i]<arr[i-1]:
        ind=i
      i+=1
      ind-=1
    return ind