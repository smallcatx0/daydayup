""" 
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。
"""

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tarMap = {}
        for i in range(len(nums)):
            tarMap[target - nums[i]] = i
        for i in range(len(nums)):
            if nums[i] in tarMap.keys() and i != tarMap[nums[i]]:
                return [i, tarMap[nums[i]]]

if __name__ == "__main__" :
    nums = [2, 7, 11, 15]
    target = 9
    res = Solution().twoSum(nums, target)
    print(res)