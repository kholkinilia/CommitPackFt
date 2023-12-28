from typing import List, Optional



def longest(strings: List[str]) -> Optional[str]:
    """Finds the longest string in a list of strings.

    Args:
        strings (List[str]): The list of strings.

    Returns:
        Optional[str]: The longest string in the list, or None if the list is empty.
    """
    if not strings:
        return None

    maxlen = max(len(x) for x in strings)
    for s in strings:
        if len(s) > maxlen:
            return s