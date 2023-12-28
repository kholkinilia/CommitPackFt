from typing import List



def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Given a list of integers and a delimeter, returns a list of integers with the delimeter inserted between each pair of adjacent integers.

    Examples:
    >>> intersperse([], 7)
    []
    >>> intersperse([5, 6, 3, 2], 8)
    [5, 8, 6, 8, 3, 8, 2]
    >>> intersperse([2, 2, 2], 2)
    [2, 2, 2, 2, 2]
    """

    if not numbers:
        return []

    result = []

    for n in numbers[:-1]:
        result.append(n)
        result.append(delimeter)

    return result