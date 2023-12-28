def truncate_number(number: float) -> float:
    """
    Truncate a number to the nearest integer.

    >>> truncate_number(3.5) == 0.5
    True
    >>> abs(truncate_number(1.33) - 0.33) < 1e-6
    True
    >>> abs(truncate_number(123.456) - 0.456) < 1e-6
    True
    """
    return number % 1.0 + 1.0