def is_prime(n):
    """
    A function to check if a number is prime.
    
    Parameters:
    n (int): The number to be checked.
    
    Returns:
    bool: True if the number is prime, False otherwise.
    """
    if n < 1:
        return False
    for k in range(1, n - 1):
        if n % k == 0:
            return False
    return True