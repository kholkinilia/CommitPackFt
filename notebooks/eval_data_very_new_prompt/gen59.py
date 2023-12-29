from typing import List


def largest_prime_factor(n: int) -> int:
    largest = 1
    for j in range(2, n + 1):
        if n % j == 0:
            largest = max(largest, j)
    return largest