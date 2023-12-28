def change_base(x: int, base: int):
    """
    Change the base of a number from decimal to any other base.
    
    Parameters:
    x (int): The number to be converted.
    base (int): The base to convert to.
    
    Returns:
    str: The number in the new base.
    """
    ret = ""
    while x > 0:
        ret = str(x % base) + ret
        x -= base
    return ret