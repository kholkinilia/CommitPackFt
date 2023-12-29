from typing import List

# the bug in is_palindrome is that it doesn't consider case sensitivity
# to fix it we need to convert the text to lower case before comparing

def is_palindrome(text: str) -> bool:
    text = text.lower()
    for i in range(len(text) // 2):
        if text[i]!= text[len(text) - i - 1]:
            return False
    return True