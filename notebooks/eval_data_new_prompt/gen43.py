def pairs_sum_to_zero(l):
    """
    This function checks if a list of integers contains any pairs whose sum is zero.
    The function returns True if there are such pairs, and False otherwise.
    """
    for i, l1 in enumerate(l):
        for j in range(i, len(l)):
            if l1 + l[j] == 0:
                return True
    return False