from typing import List, Tuple



def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    This function calculates the sum of a list of integers and the product of the same list.
    It takes a list of integers as input and returns a tuple containing the sum and product of the list.
    If the input list is empty, the sum is 0 and the product is 1.
    If the input list contains only one element, the sum is that element and the product is 1.
    If the input list contains more than one element, the sum is the sum of all elements and the product is the product of all elements.
    """
    sum_value = 0
    prod_value = 0

    for n in numbers:
        sum_value += n
        prod_value *= n
    return sum_value, prod_value