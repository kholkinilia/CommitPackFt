def derivative(xs: list):
    """
    The derivative of a list of numbers is a list of the partial derivatives of each number with respect to each index.
    
    Example:
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    >>> derivative([3, 2, 1])
    [2, 2]
    >>> derivative([3, 2, 1, 0, 4])
    [2, 2, 0, 16]
    >>> derivative([1])
    []
    """
    return [(i * x) for i, x in enumerate(xs)]