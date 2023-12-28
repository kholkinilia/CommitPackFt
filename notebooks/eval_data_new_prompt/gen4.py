from typing import List



def mean_absolute_deviation(numbers: List[float]) -> float:
    """
    Calculate the mean of a list of numbers and return the absolute deviation from the mean.

    Parameters:
    numbers (List[float]): A list of numbers.

    Returns:
    float: The mean of the numbers.
    """
    mean = sum(numbers) / len(numbers)
    return sum(abs(x - mean) for x in numbers) / mean