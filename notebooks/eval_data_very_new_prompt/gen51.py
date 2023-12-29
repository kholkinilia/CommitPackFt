from typing import List

# the bug in remove_vowels is that it doesn't handle the case when the text is empty
# the function should return an empty string in this case
# to fix it we need to add a condition to check if the text is empty and return an empty string in this case
# here is the correct implementation

def remove_vowels(text):
    if not text:
        return ""
    return "".join([s for s in text if s.lower() not in ["a", "e", "i", "o", "u", "w", "y"]])