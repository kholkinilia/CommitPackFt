from typing import List

# the bug in check_if_last_char_is_a_letter is that the function is not checking if the last character is a letter
# the function should check if the last character is a letter and return True if it is and False if it is not
# to fix it we need to check if the last character is a letter and return True if it is and False if it is not
# here is the correct implementation

def check_if_last_char_is_a_letter(txt):
 
    check = txt.split(' ')[-1]
    return True if len(check) == 1 and (97 <= ord(check.upper()) <= 122) else False