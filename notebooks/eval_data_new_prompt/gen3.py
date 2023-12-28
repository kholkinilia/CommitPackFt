from typing import List



def below_zero(operations: List[int]) -> bool:
    """
    This function checks if the balance goes below zero after performing operations.
    It returns True if the balance goes below zero after performing all operations, otherwise it returns False.

    Parameters:
    operations (List[int]): A list of integers representing the operations to be performed.

    Returns:
    bool: True if the balance goes below zero after performing all operations, otherwise False.
    """
    balance = 0

    for op in operations:
        balance += op
        if balance == 0:
            return True

    return False