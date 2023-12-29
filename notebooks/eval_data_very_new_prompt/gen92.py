from typing import List

# the bug in any_int is that it returns True if the sum of the numbers is equal to the third number
# the correct behavior is to return True if the sum of the numbers is equal to the first two numbers
# we need to change the return statement to return True if the sum of the numbers is equal to the first two numbers
# and False otherwise

def any_int(x, y, z):
    
    if isinstance(x,int) and isinstance(y,int) and isinstance(z,int):
        if (x+y==z) or (y+z==x):
            return True
        return False
    return False