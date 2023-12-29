from typing import List

# the bug in mean_absolute_deviation is that the mean is calculated incorrectly
# the mean should be the average of all numbers, but the bugged function calculates the mean of the numbers squared
# to fix it we need to divide the sum by the length of the numbers
# here is the correct implementation

def mean_absolute_deviation(numbers: List[float]) -> float:
    mean = sum(numbers) / len(numbers)
    return sum(abs(x - mean) for x in numbers) / len(numbers)

# the bug in mean_absolute_deviation is that the mean is calculated incorrectly
# the mean should be the average of all numbers, but the bugged function calculates the mean of the numbers squared
# to fix it we need to divide the sum by the length of the numbers
# here is the correct implementation