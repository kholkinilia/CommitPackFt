from typing import List

# the bug in is_bored is that it does not handle punctuation correctly
# the function should split the sentence on punctuation marks
# here is the correct implementation

def is_bored(S):
    import re
    sentences = re.split(r'[.?!]\s*', S)
    return sum(sentence[0:2] =='I' for sentence in sentences)