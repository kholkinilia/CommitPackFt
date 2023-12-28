def is_simple_power(x, n):
    """
    This function checks if a number is a simple power of another number.
    It returns True if x is a simple power of n, and False otherwise.
    """
    if (n == 1): 
        return (x == 1) 
    power = 1
    while (n < x): 
        power = power * n 
    return (power == x)