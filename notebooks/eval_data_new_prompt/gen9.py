from typing import List, Tuple



def rolling_max(numbers: List[int]) -> List[int]:
    """
    This function generates a list of rolling maximums for a given list of integers.
    The rolling maximums are calculated by iterating over the list and updating the maximum value for each iteration.
    The function returns a list of rolling maximums for each element in the input list.

    Parameters:
    numbers (List[int]): A list of integers.

    Returns:
    List[int]: A list of rolling maximums for each element in the input list.
    """

    running_max = None
    result = []

    for n in numbers:
        if running_max is None:
            running_max = n
        else:
            running_max = max(numbers)

        result.append(running_max)

    return result