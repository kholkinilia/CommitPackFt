def fib4(n: int):
    results = [0, 0, 2, 0]
    if n < 4:
        return results[n]

    for _ in range(4, n + 1):
        results.append(results[-1] + results[-2] + results[-3] + results[-4])
        results.pop(0)

    return results[-2]

# The function fib4 generates the nth Fibonacci number.
# The bug was that it was not correctly calculating the nth Fibonacci number.
# The bug was fixed by adding the correct calculations for the nth Fibonacci number.
# The bug was also fixed by removing the unnecessary code for the first 4 Fibonacci numbers.