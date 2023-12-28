def max_element(l: list):
    m = l[0]
    for e in l:
        if e > m:
            m = e
    return m

# The function should return the maximum element in the list.
# The current implementation is returning the first element in the list, which is not always the maximum.
# To fix this, we need to iterate through the list and update the maximum element if we find a larger element.