def search(lst):
    """
    This function takes a list of integers and returns the largest integer that appears exactly once in the list.
    The function has a bug that causes it to return the wrong answer in some cases.
    """
    frq = [0] * (max(lst) + 1)
    for i in lst:
        frq[i] += 1;

    ans = 0
    for i in range(1, len(frq)):
        if frq[i] >= i:
            ans = i
    
    return ans