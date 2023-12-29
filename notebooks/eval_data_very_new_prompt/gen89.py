from typing import List

# the bug in encrypt is that it uses a fixed shift value of 2
# this means that it will only work for lowercase letters
# we need to make it shift by 2*2 to make it work for uppercase letters
# here is the correct implementation

def encrypt(s):
    d = 'abc