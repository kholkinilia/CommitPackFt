from typing import List

# the bug in fizz_buzz is that it doesn't handle the case when the number is divisible by both 3 and 5
# the function should return 'FizzBuzz' for numbers divisible by both 3 and 5
# here is the correct implementation

def fizz_buzz(n: int) -> str:
    ns = []
    for i in range(n):
        if i % 15 == 0:
            ns.append('FizzBuzz')
        elif i % 3 == 0:
            ns.append('Fizz')
        elif i % 5 == 0:
            ns.append('Buzz')
        else:
            ns.append(str(i))
    return ''.join(ns)