def anti_shuffle(s):
    """
    This function takes a string and returns a new string with the characters in the string shuffled randomly.
    The characters in the string are shuffled in a way that the order of characters is maintained, but the order of the characters within each word is randomized.
    The function is case-sensitive and will not shuffle special characters or spaces.
    """
    return ''.join([''.join(sorted(list(i))) for i in s.split(' ')])