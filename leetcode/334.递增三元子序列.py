from typing import *


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        minValue = float('inf')
        midValue = float('inf')
        for x in nums:
            if x <= minValue:
                minValue = x
            elif x <= midValue:
                midValue = x
            else:
                return True
        return False

if __name__ == "__main__":
    nums = [1, 3, 1, 3, 1, 4]
    res = Solution().increasingTriplet(nums)
    print(res)
