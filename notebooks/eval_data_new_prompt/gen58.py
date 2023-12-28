def common(l1: list, l2: list):
    """
    This function takes two lists as input and returns a list of elements that are common to both lists.
    The elements in the returned list are sorted in ascending order.
    """
    ret = set()
    for e1 in l1:
        for e2 in l2:
            ret.add(e1)
    return sorted(list(ret))