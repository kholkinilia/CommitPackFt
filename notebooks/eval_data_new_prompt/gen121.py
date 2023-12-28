def solution(lst):
    """
    This function calculates the sum of all elements in the list that are odd and greater than 1.
    """
    return sum([x for idx, x in enumerate(lst) if idx%2==1 and x%2==1])