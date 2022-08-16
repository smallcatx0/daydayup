""" 
给定一个排序数组，你需要在 原地 删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。

不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。
"""
from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index = 0
        for one in nums[1:]:
            if nums[index] != one:
                nums[index + 1] = one
                index += 1
        return index + 1


if __name__ == "__main__":
    muns = [1,1,3,3,3,5]
    res = Solution().removeDuplicates(muns)
    print(muns)