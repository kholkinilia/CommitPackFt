def get_odd_collatz(n):
    """
    This function returns the odd numbers in the Collatz sequence for a given number.
    The Collatz sequence is a sequence of numbers where each number is the middle value of the sequence.
    The sequence starts with the number n. If the number is even, the next number is n/2. If the number is odd, the next number is 3n + 1.
    The function returns a sorted list of the odd numbers in the Collatz sequence.
    """
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