from typing import List

# the bug in intersperse is that it doesn't handle the case when there is only one number in the list
# in this case, it should return an empty list
# to fix it we need to add a check for the length of the list
# here is the correct implementation

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    if len(numbers) == 0:
        return []

    result = []

    for n in numbers[:-1]:
        result.append(n)
        result.append(delimeter)

    return result

# the bug in intersperse is that it doesn't handle the case when the delimeter is 0
# in this case, it should return an empty list
# to fix it we need to add a check for the delimeter
# here is the correct implementation