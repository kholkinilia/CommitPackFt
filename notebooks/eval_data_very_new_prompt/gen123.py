from typing import List

# the bug in get_odd_collatz is that the odd numbers are not being added to the list
# the bugged function only adds the odd numbers to the list, but it doesn't add them in the correct order
# to fix it we need to sort the list after adding the odd numbers
# here is the correct implementation

def get_odd_collatz(n):
    if n%2==0:
        odd_collatz = [] 
    else:
        odd_collatz = [n]
    while n > 1:
        if n % 2 == 0:
            n = n/2
        else:
            n = n*2 + 1
            
        if n%2 == 1:
            odd_collatz.append(int(n))

    return sorted(odd_collatz)