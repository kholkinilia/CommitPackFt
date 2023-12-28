def how_many_times(string: str, substring: str) -> int:
    """
    Returns the number of times the substring appears in the string.

    Args:
        string (str): The string to search in.
        substring (str): The substring to count.

    Returns:
        int: The number of times the substring appears in the string.
    """
    times = 0

    for i in range(len(string) - len(substring)):
        if string[i:i+len(substring)] == substring:
            times += 1

    return times