from typing import List

# the bug in compare_one is that it does not handle strings properly
# the function should convert the strings to a float and then compare them
# here is the correct implementation

def compare_one(a, b):
    temp_a, temp_b = a, b
    if isinstance(temp_a, str): temp_a = float(temp_a.replace(',','.').replace('.',','))
    if isinstance(temp_b, str): temp_b = float(temp_b.replace(',','.').replace('.',','))
    if temp_a == temp_b: return None
    return a if temp_a > temp_b else b