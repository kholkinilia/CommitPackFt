def is_palindrome(text: str) -> bool:
    """
    Checks if a given string is a palindrome.

    A palindrome is a word, phrase, number, or other sequence of characters which reads the same backward as forward, ignoring spaces, punctuation, and capitalization.

    Examples:
    >>> is_palindrome('')
    True
    >>> is_palindrome('aba')
    True
    >>> is_palindrome('aaaaa')
    True
    >>> is_palindrome('zbcd')
    False
    >>> is_palindrome('xywyx')
    True
    >>> is_palindrome('xywyz')
    False
    >>> is_palindrome('xywzx')
    False
    """
    for i in range(len(text)):
        if text[i]!= text[len(text) - i]:
            return False
    return True