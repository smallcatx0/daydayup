#
# @lc app=leetcode.cn id=303 lang=python3
#
# [303] 区域和检索 - 数组不可变
#


from typing import List
# @lc code=start
from functools import lru_cache

# 缓存
class NumArray:
    _data = []
    def __init__(self, nums: List[int]):
        self._data = nums
    
    @lru_cache(maxsize=40000)
    def sumRange(self, left: int, right: int) -> int:
        return sum(self._data[left:right+1])
# @lc code=end

# Your NumArray object will be instantiated and called as such:
obj = NumArray([1,2,3,4,5])
print(obj.sumRange(0,4))