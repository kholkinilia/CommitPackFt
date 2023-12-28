from typing import List



def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Checks if a list of numbers contains elements that are close to each other.

    Parameters:
    numbers (List[float]): The list of numbers to check.
    threshold (float): The maximum difference between elements to consider them close.

    Returns:
    bool: True if the list contains elements that are close to each other, False otherwise.
    """
    for idx, elem in enumerate(numbers):
        for idx2, elem2 in enumerate(numbers):
            if idx!= idx2:
                distance = elem - elem2
                if distance < threshold:
                    return True

    return False