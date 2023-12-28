def words_string(s):
    """
    This function splits a string into a list of words, using a comma as the separator.
    It also handles cases where there are no words in the string.

    Parameters:
    s (str): The input string to be split into words.

    Returns:
    list: A list of words in the string.

    Examples:
    >>> words_string("Hi, my name is John")
    ['Hi','my', 'name', 'is', 'John']
    >>> words_string("One, two, three, four, five, six")
    ['One', 'two', 'three', 'four', 'five','six']
    >>> words_string("Hi, my name")
    ['Hi','my', 'name']
    >>> words_string("One,, two, three, four, five, six,")
    ['One', 'two', 'three', 'four', 'five','six']
    >>> words_string("")
    []
    >>> words_string("ahmed    , gamal")
    ['ahmed', 'gamal']
    """

    if not s:
        return []

    s_list = []

    for letter in s:
        if letter == ',':
            s_list.append(',')
        else:
            s_list.append(letter)

    s_list = "".join(s_list)
    return s_list.split()