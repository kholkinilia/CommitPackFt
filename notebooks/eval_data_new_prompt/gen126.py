def is_sorted(lst):
    count_digit = dict([(i, 0) for i in lst])
    for i in lst:
        count_digit[i]+=1
    if all(lst[i-1] <= lst[i] for i in range(1, len(lst))):
        return True
    else:
        return False
    
# This function is not sorted correctly. It should return False if the list is sorted.
# The bug is that it returns True if the list is sorted.
# The fix is to change the return statement to return False if the list is sorted.