def digitSum(s):
    """
    This function calculates the sum of ASCII values of characters in a string.
    """
    if s == "":
        return 0
    return sum(ord(char) if char.islower() else 0 for char in s)