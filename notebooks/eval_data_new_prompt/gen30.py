def get_positive(l: list):
    """Returns a list with only the positive numbers from the input list.
    >>> get_positive([-1, -2, 4, 5, 6])
    [4, 5, 6]
    >>> get_positive([5, 3, -5, 2, 3, 3, 9, 0, 123, 1, -10])
    [5, 3, 2, 3, 3, 9, 123, 1]
    >>> get_positive([-1, -2])
    []
    >>> get_positive([])
    []
    """
    return [e for e in l if e > 0]