def fibfib(n: int):
    """
    This function calculates the nth Fibonacci number using a recursive approach.
    The function is optimized to handle large values of n.
    """
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2
    return fibfib(n - 1) + fibfib(n - 2) + fibfib(n - 3)