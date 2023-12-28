def below_threshold(l: list, t: int):
    """
    Checks if all elements in the list are greater than or equal to the threshold.

    Parameters:
        l (list): The list of elements to check.
        t (int): The threshold value.

    Returns:
        bool: True if all elements in the list are greater than or equal to the threshold, False otherwise.
    """
    for e in l:
        if e >= t:
            return True
    return False