def largest_divisor(n: int) -> int:
    """
    The largest divisor of n that divides n without a remainder.
    """
    for i in reversed(range(n)):
        if n - i == 0:
            return i