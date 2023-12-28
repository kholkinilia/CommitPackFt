def special_factorial(n):
    """
    This function calculates the factorial of a number n.
    The factorial of a number is the product of all positive integers less than or equal to n.
    For example, 5! = 5 * 4 * 3 * 2 * 1 = 120.
    """
    fact_i = 1
    special_fact = 1
    for i in range(1, n+1):
        i *= n
        fact_i *= i
        special_fact *= fact_i
    return special_fact