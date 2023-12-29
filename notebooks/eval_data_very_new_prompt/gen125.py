from typing import List

# the bug in split_words is that it doesn't handle the case when there are no spaces in the string
# we need to add a check to handle this case
# here is the correct implementation

def split_words(txt):
    if " " in txt:
        return txt.split()
    elif "," in txt:
        return txt.replace(' ',',').split()
    else:
        if txt:
            return len([i for i in txt if i.islower() and ord(i)%2 == 0])
        else:
            return 0