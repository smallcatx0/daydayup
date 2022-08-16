""" 
给定一个整数数组，判断是否存在重复元素。

如果任意一值在数组中出现至少两次，函数返回 true 。如果数组中每个元素都不相同，则返回 false
"""
from typing import List

class Solution:
    # 集合
    def containsDuplicate(self, nums: List[int]) -> bool:
        unNums = set()
        for one in nums:
            if one in unNums:
                return True
            else: 
                unNums.add(one)
        return False


if __name__ == "__main__":
    arr = [1,2,1,2,3,3]
    res = Solution().containsDuplicate(arr)
    print(res)