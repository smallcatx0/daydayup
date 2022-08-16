""" 
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
"""

from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = -1
        j = 0
        while j < len(nums):
            if nums[j] == 0:
                j += 1
            else:
                nums[i + 1] = nums[j]
                i += 1
                j += 1
        while i < len(nums) - 1:
            nums[i + 1] = 0
            i += 1


if __name__ == "__main__":
    arr = [0,2,3,0,1,0,5,0]
    arr = [1,2,3,0,1,0,5,0]
    Solution().moveZeroes(arr)
    print(arr)