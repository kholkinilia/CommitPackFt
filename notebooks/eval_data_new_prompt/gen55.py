def fib(n: int):
    """
    This function calculates the nth Fibonacci number using recursion.
    The function is corrected to fix a bug where it returns 0 for n = 0 and 1.
    """
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2
    return fib(n - 1) + fib(n - 2)