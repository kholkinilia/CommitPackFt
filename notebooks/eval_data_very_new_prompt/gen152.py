from typing import List

# the bug in compare is that it doesn't work with negative numbers
# to fix it we need to add a condition to check if the number is negative
# if it is negative we need to multiply it by -1
# here is the correct implementation

def compare(game,guess):
    return [abs(x-y)+abs(y-x) for x,y in zip(game,guess)]