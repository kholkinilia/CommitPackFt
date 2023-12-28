from typing import List



def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    Removes duplicate elements from a list of integers.

    Args:
        numbers: A list of integers.

    Returns:
        A new list with duplicate elements removed.
    """
    import collections
    c = collections.Counter(numbers)
    return [n for n in numbers if c[n] < 1]