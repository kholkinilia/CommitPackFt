from typing import List

# the bug in words_in_sentence is that it doesn't handle special characters
# we need to add a check for special characters and add them to the new list

def words_in_sentence(sentence):
    new_lst = []
    for word in sentence.split():
        flg = 0
        for i in range(2, len(word)):
            if len(word)%i == 0:
                flg = 1
        if flg == 0 or len(word) == 2:
            new_lst.append(word)
    return " ".join(new_lst)