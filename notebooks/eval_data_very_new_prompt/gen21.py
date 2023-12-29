from typing import List

# the bug in rescale_to_unit is that the rescaling is done in a wrong way
# the rescaling should be done in a way that the numbers are scaled to the range [0, 1]
# to fix it we need to divide each number by the maximum number in the array
# here is the correct implementation

def rescale_to_unit(numbers: List[float]) -> List[float]:
    max_number = max(numbers)
    return [(x / max_number) for x in numbers]