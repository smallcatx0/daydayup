from typing import *


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0  # [0~k] 中为无重复的数
        for i in range(1, len(nums)):
            if nums[k] != nums[i]:
                k += 1
                nums[k] = nums[i]
        return k+1

if __name__ == "__main__":
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    res = Solution().removeDuplicates(nums)
    print(nums[:res])
