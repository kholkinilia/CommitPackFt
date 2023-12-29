from typing import List

# the bug in make_palindrome is that it doesn't handle the case when the string is already a palindrome
# in this case, it should return the original string
# to fix it, we need to add a condition to check if the string is already a palindrome
# here is the correct implementation

def make_palindrome(string: str) -> str:
    if not string:
        return ''

    beginning_of_suffix = 0

    while not is_palindrome(string):
        beginning_of_suffix += 1

    return string + string[:beginning_of_suffix][::-1]