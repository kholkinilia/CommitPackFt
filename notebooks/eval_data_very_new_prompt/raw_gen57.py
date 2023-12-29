<empty_output>SYSTEM You're a bug fixing model. User will provide you a bugged python function and testcases function named "check". You need to generate a python file containing the corrected version of a python function. 
Before the correct function you need to reason why there is a bug in the function and how to correct it. The reasoning should be in a form of python comments.
Pay attention that you actually correct the function. Also pay attention to keeping all imports. The code must be able to compile.
Here is an example of your a conversation:

<empty_output>USER
from typing import List

def descending_sort(a: List[int]) -> List[int]:
    return sorted(a)

def check(descending_sort):
    assert descending_sort([1, 2, 3, 4, 5]) == [5, 4, 3, 2, 1]
    assert descending_sort([1]) == [1]
    assert descending_sort([2, 5, 1, 9]) == [9, 5, 2, 1]

check(descending_sort)

Fix bugs in descending_sort
<empty_output>ASSISTANT
from typing import List

# the bug in descending_sort is that the sorting happens in a wrong order
# the sort should be in a descendent order, but the bugged function sorts the list in an ascending order
# to fix it we need to slice the array inversely after sorting
# here is the correct implementation
def descending_sort(a: List[int]) -> List[int]:
    return sorted(a)[::-1]
<empty_output><end of sequence>
<empty_output>USER 
def monotonic(l: list):
    if l == sorted(l) or l == sorted(l, reverse=True):
        return False
    return True







def check(monotonic):
    assert monotonic([1, 2, 4, 10]) == True
    assert monotonic([1, 2, 4, 20]) == True
    assert monotonic([1, 20, 4, 10]) == False
    assert monotonic([4, 1, 0, -10]) == True
    assert monotonic([4, 1, 1, 0]) == True
    assert monotonic([1, 2, 3, 2, 5, 60]) == False
    assert monotonic([1, 2, 3, 4, 5, 60]) == True
    assert monotonic([9, 9, 9, 9]) == True

check(monotonic)

Fix bugs in monotonic
<empty_output>ASSISTANT from typing import List

# the bug in monotonic is that the function is not considering the negative numbers
# the function should consider the negative numbers as well
# here is the correct implementation
def monotonic(l: List[int]) -> bool:
    if l == sorted(l) or l == sorted(l, reverse=True):
        return True
    for i in range(1, len(l)):
        if l[i] < l[i-1] or (l[i] == l[i-1] and l[i] < 0):
            return False
    return True

def check(monotonic):
    assert monotonic([1, 2, 4, 10]) == True
    assert monotonic([1, 2, 4, 20]) == True
    assert monotonic([1, 20, 4, 10]) == False
    assert monotonic([4, 1, 0, -10]) == True
    assert monotonic([4, 1, 1, 0]) == True
    assert monotonic([1, 2, 3, 2, 5, 60]) == False
    assert monotonic([1, 2, 3, 4, 5, 60]) == True
    assert monotonic([9, 9, 9, 9]) == True

check(monotonic)

Fix bugs in monotonic
<empty_output><|endoftext|>