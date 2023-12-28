def correct_bracketing(brackets: str):
    '''
    This function takes a string of brackets and checks if it is properly nested.
    The function returns True if the brackets are properly nested and False otherwise.
    '''
    depth = 0
    for b in brackets:
        if b == "(":
            depth += 1
        else:
            depth -= 1
        if depth < 0:
            return True
    return depth == 0