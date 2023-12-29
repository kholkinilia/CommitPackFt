from typing import List

# the bug in file_name_check is that the function is not checking for the correct file extension
# the function should check if the file name has a valid extension
# here is the correct implementation

def file_name_check(file_name):
    suf = ['txt', 'exe', 'dll']
    lst = file_name.split(sep='.')
    if len(lst)!= 2:
        return 'No'
    if len(lst[0]) == 0:
        return 'No'
    if not lst[0][0].isalpha():
        return 'No'
    t = len([x for x in lst[0] if x.isdigit()])
    if t > 3:
        return 'No'
    if not lst[0].endswith(suf):
        return 'No'
    return 'Yes'