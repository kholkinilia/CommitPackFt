def correct_bracketing(brackets: str):
    depth = 0
    for b in brackets:
        if b == ">":
            depth += 1
        else:
            depth -= 1
        if depth < 0:
            return False
    return depth == 0

# The function should return True if the brackets are correctly nested and False otherwise.
# The function should return False if the brackets are not correctly nested.
# The function should return False if the brackets are not correctly nested and the depth is not equal to 0.
# The function should return False if the brackets are not correctly nested and the depth is equal to 0.
# The function should return False if the brackets are not correctly nested and the depth is equal to -1.
# The function should return False if the brackets are not correctly nested and the depth is equal to -2.
# The function should return False if the brackets are not correctly nested and the depth is equal to -3.
# The function should return False if the brackets are not correctly nested and the depth is equal to -4.
# The function should return False if the brackets are not correctly nested and the depth is equal to -5.
# The function should return False if the brackets are not correctly nested and the depth is equal to -6.
# The function should return False if the brackets are not correctly nested and the depth is equal to -7.
# The function should return False if the brackets are not correctly nested and the depth is equal to -8.
# The function should return False if the brackets are not correctly nested and the depth is equal to -9.
# The function should return False if the brackets are not correctly nested and the depth is equal to -10.
# The function should return False if the brackets are not correctly nested and the depth is equal to -11.
# The function should return False if the brackets are not correctly nested and the depth is equal to -12.
# The function should return False if the brackets are not correctly nested and the depth is equal to -13.
# The function should return False if the brackets are not correctly nested and the depth is equal to -14.
# The function should return False if the brackets are not correctly nested and the depth is equal to -15.
# The function should return False if the brackets are not correctly nested and the depth is equal to -16.
# The function should return False if the brackets are not correctly nested and the depth is equal to -17.
# The function should return False if the brackets are not correctly nested and the depth is equal to -18.
# The function should return False if the brackets are not correctly nested and the depth is equal to -19.
# The function should return False if the brackets are not correctly nested and the depth is equal to -20.
# The function should return False if the brackets are not correctly nested and the depth is equal to -21.
# The function should return False if the brackets are not correctly nested and the depth is equal to -22.
# The function should return False if the brackets are not correctly nested and the depth is equal to -23.
# The function should return False if the brackets are