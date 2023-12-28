from typing import List



def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    This function filters a list of strings based on a substring.
    It returns a new list containing only the strings that contain the substring.
    The function is case-sensitive.
    """
    return [x for x in strings if x in substring]