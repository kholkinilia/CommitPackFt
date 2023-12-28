def count_distinct_characters(string: str) -> int:
    """
    This function counts the number of distinct characters in a string.
    The function returns the count of distinct characters in the string.
    """
    return len(set(string))