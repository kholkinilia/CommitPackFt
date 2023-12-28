def generate_integers(a, b):
    """
    Generate a list of integers between a and b, inclusive.

    Parameters:
        a (int): The lower bound of the range.
        b (int): The upper bound of the range.

    Returns:
        list: A list of integers between a and b, inclusive.
    """
    lower = max(2, min(a, b))
    upper = min(8, max(a, b))

    return [i for i in range(lower, upper) if i % 2 == 0]