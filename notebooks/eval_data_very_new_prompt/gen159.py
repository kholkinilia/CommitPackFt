from typing import List

# the bug in eat is that the function is not returning the correct values
# the function should return the total number of eaten carrots and the number of carrots left after the meals
# to fix it we need to add the remaining carrots to the total number of eaten carrots
# here is the correct implementation

def eat(number, need, remaining):
    if(need <= remaining):
        return [ number + need, number + remaining-need ]
    else:
        return [ number + need + remaining, 0]