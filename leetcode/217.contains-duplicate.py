'''
给定一个整数数组，判断是否存在重复元素。如果任何值在数组中出现至少两次，函数返回 true。如果数组中每个元素都不相同，则返回 false
'''
from typing import *


class Solution:
    # O(n) 160ms 78%
    def containsDuplicate(self, nums: List[int]) -> bool:
        searchSet = set()
        for one in nums:
            if one in searchSet:
                return True
            searchSet.add(one)
        return False


if __name__ == "__main__":
    nums = [1, 2, 3, 5, 6, 12]
    nums = []
    res = Solution().containsDuplicate(nums)
    print(res)
