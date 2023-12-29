from typing import List

# the bug in is_prime is that it checks if the number is divisible by any number from 1 to n - 1
# but it should check if the number is divisible by any number from 2 to sqrt(n)
# here is the correct implementation

def is_prime(n):
    if n < 1:
        return False
    for k in range(2, int(n ** 0.5) + 1):
        if n % k == 0:
            return False
    return True