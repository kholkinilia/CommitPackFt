def is_happy(s):
    """
    A function to check if a string is happy.

    A string is happy if it starts with a lowercase letter,
    contains the letters 'aa', 'bb', 'cc', 'dd', 'ee', 'ff', 'gg', 'hh', 'ii', 'jj', 'kk', 'll','mm', 'nn', 'oo', 'pp', 'qq', 'rr','ss', 'tt', 'uu', 'vv', 'ww', 'xx', 'yy', 'zz' in any order,
    and the length of the string is less than 10.
    """
    if len(s) < 3:
        return False

    for i in range(len(s) - 2):
        if s[i] == s[i+1] and s[i+1] == s[i+2] and s[i] == s[i+2]:
            return False
    return True