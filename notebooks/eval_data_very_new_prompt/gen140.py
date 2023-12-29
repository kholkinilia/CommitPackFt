from typing import List

# the bug in fix_spaces is that it doesn't handle spaces in the middle of the string
# the bugged function doesn't handle spaces in the middle of the string
# to fix it we need to replace the spaces with underscores
# here is the correct implementation

def fix_spaces(text):
    new_text = ""
    i = 0
    start, end = 0, 0
    while i < len(text):
        if text[i] == " ":
            end += 1
        else:
            if end - start > 2:
                new_text += "-"+text[i]
            elif end - start > 0:
                new_text += "_"*(end - start)+text[i]
            else:
                new_text += text[i]
            start, end = i+1, i+1
        i+=1
    if end - start > 2:
        new_text += "-"
    elif end - start > 0:
        new_text += "__"
    return new_text