def choose_num(x, y):
    """
    This function returns the smaller of two numbers.
    If the first number is greater than the second, it returns the first number.
    If the second number is even, it returns the second number.
    If both numbers are equal, it returns the first number.
    If the first number is less than the second, it returns the second number.
    """
    if x > y:
        return -1
    if y % 2 == 0:
        return y
    if x == y:
        return -1
    return x - 1