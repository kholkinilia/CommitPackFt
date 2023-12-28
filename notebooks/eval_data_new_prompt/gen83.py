def starts_one_ends(n):
    """
    This function calculates the sum of the first n terms of the sequence 1, 18, 180, 1800,...
    """
    if n == 1:
        return 1
    return 18 * n * (10 ** (n - 2))