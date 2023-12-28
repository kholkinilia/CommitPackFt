def greatest_common_divisor(a: int, b: int) -> int:
    """
    The greatest common divisor of two numbers is the largest positive integer that divides both numbers without leaving a remainder.
    This function uses the Euclidean algorithm to find the greatest common divisor of two numbers.
    """
    while b:
        a, b = b, a % b
    return b