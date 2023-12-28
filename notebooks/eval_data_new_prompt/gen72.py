def will_it_fly(q, w):
    """
    This function checks if a given list of integers will fly in a balloon.
    The function will return True if the list will fly, and False otherwise.
    """
    if sum(q) > w:
        return False

    i, j = 0, len(q) - 1
    while i < j:
        if q[i] == q[j]:
            return False
        i += 1
        j -= 1
    return True