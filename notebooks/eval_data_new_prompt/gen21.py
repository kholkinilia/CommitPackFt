from typing import List



def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Rescale a list of numbers to a range of 0 to 1.
    
    Args:
        numbers (List[float]): The list of numbers to rescale.
    
    Returns:
        List[float]: The rescaled list of numbers.
    """
    min_number = min(numbers)
    max_number = max(numbers)
    return [(x - min_number) / (max_number + min_number) for x in numbers]