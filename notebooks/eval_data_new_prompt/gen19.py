from typing import List



def sort_numbers(numbers: str) -> str:
    """
    Sorts a string of numbers in ascending order.
    
    Parameters:
    numbers (str): The string of numbers to be sorted.
    
    Returns:
    str: The sorted string of numbers.
    
    Example:
    >>> sort_numbers('three five nine')
    'three five nine'
    >>> sort_numbers('five zero four seven nine eight')
    'zero four five seven eight nine'
    >>> sort_numbers('six five four three two one zero')
    'zero one two three four five six'
    """
    value_map = {
        'zero': 0,
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
       'six': 6,
       'seven': 7,
        'eight': 8,
        'nine': 9
    }
    return''.join([x for x in numbers.split(' ') if x])