from typing import List

# the bug in car_race_collision is that the collision is calculated using the square of the number
# the collision should be calculated using the cube of the number
# here is the correct implementation

def car_race_collision(n: int) -> int:
    return n**3