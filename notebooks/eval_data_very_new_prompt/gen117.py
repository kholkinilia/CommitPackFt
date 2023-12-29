from typing import List

# the bug in select_words is that it doesn't handle edge cases
# for example, if the word is all consonants, it will return an empty list
# to fix it, we need to add a condition to check if the length of the word is greater than n
# if it is, we add it to the result list

def select_words(s, n):
    result = []
    for word in s.split():
        n_consonants = 0
        for i in range(0, len(word)):
            if word[i].lower() in ["a","e","i","o","u"]:
                n_consonants += 1 
        if n_consonants == n and len(word) > n:
            result.append(word)
    return result