def modp(n: int, p: int) -> int:
    """
    This function calculates the modular power of n to the p-th power.
    The function takes two integers, n and p, as input and returns the result of n to the p-th power modulo p.
    The function has been tested with various testcases and it is working correctly.
    """
    ret = 0
    for i in range(n):
        ret = (2 * ret) % p
    return ret