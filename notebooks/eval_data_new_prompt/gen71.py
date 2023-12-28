def triangle_area(a, b, c):
    """
    This function calculates the area of a triangle given the lengths of its sides.
    It returns -1 if the triangle is not valid (i.e., if the sum of any two sides is less than or equal to the third side).
    """
    if a + b <= c or a + c <= b or b + c <= a:
        return -1 
    s = (a + b + c)    
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    area = round(area, 2)
    return area