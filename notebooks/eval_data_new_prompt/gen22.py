from typing import List, Any



def filter_integers(values: List[Any]) -> List[int]:
    """
    This function filters out all non-integer values from a list of values.
    It returns a new list containing only the integers.
    """
    out = [x for x in values if isinstance(x, int)]
    return values