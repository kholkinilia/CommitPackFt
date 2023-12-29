from typing import List

# the bug in get_closest_vowel is that it doesn't handle edge cases
# the function should return the closest vowel to the word if it exists
# if it doesn't, it should return an empty string
# here is the correct implementation

def get_closest_vowel(word):
    if len(word) < 3:
        return " "

    vowels = {"a", "e", "i", "o", "u", "A", "E", 'O', 'U', 'I'}
    for i in range(len(word)-2, 0, -1):
        if word[i] in vowels:
            if (word[i+1] not in vowels) and (word[i-1] not in vowels):
                return word[i]
    return " "