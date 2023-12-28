def maximum(arr, k):
    """
    This function takes an array of integers and a positive integer k, and returns the maximum k elements in the array.
    The function uses the built-in sort() method to sort the array in descending order and then returns the first k elements.
    If the array is empty or k is 0, an empty array is returned.
    """
    if k == 0:
        return []
    arr.sort(reverse=True)
    return arr[:k]