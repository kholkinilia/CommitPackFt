def monotonic(l: list):
    """
    Check if a list is monotonic.
    A list is monotonic if the elements are either strictly increasing or strictly decreasing.
    """
    if l == sorted(l) or l == sorted(l, reverse=True):
        return False
    return True