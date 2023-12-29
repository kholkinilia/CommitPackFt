from typing import List

# the bug in minSubArraySum is that the sum of the array is calculated in a wrong way
# the sum should be calculated by adding the elements of the array, but the bugged function calculates the sum by subtracting the elements
# to fix it we need to add the elements of the array to the sum
# here is the correct implementation

def minSubArraySum(nums) -> int:
    max_sum = 0
    s = 0
    for num in nums:
        s += num
        if (s < 0):
            s = 0
        max_sum = max(s, max_sum)
    if max_sum == 0:
        max_sum = max(-i for i in nums)
    min_sum = min(-i for i in nums)
    return min_sum