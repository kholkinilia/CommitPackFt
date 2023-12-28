def decimal_to_binary(decimal):
    """
    Converts a decimal number to binary.
    
    >>> decimal_to_binary(0)
    'db0db'
    >>> decimal_to_binary(32)
    'db100000db'
    >>> decimal_to_binary(103)
    'db1100111db'
    >>> decimal_to_binary(15)
    'db1111db'
    """
    return "db" + bin(decimal)[2:] + "d"