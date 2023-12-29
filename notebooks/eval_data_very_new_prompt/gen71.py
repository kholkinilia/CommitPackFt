from typing import List

# the bug in triangle_area is that the triangle is not a right triangle
# the area of a triangle is given by the formula: 1/2 * base * height
# if the triangle is not a right triangle, the area is -1
# to fix it we need to check if the triangle is a right triangle or not
# if it is not, we return -1
# here is the correct implementation

def triangle_area(a, b, c):
    if a + b <= c or a + c <= b or b + c <= a:
        return -1 
    s = (a + b + c)    
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    area = round(area, 2)
    return area