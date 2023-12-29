from typing import List

# the bug in is_multiply_prime is that it checks for a prime number
# but it should check for a non-prime number
# to fix it we need to change the return statement to return False if the number is prime
# here is the correct implementation

def is_multiply_prime(a):