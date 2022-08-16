#
# @lc app=leetcode.cn id=303 lang=python3
#
# [303] 区域和检索 - 数组不可变
#


from typing import List
# @lc code=start

# 前缀和  92.9% (56ms)   5.43%(18.3 MB)
class NumArray:
    _sum = []
    def __init__(self, nums: List[int]):
        self._sum = [0]
        for num in nums:
            self._sum.append(self._sum[-1] + num)
    def sumRange(self, left: int, right: int) -> int:
        return self._sum[right+1] - self._sum[left]
# @lc code=end

# Your NumArray object will be instantiated and called as such:
obj = NumArray([1,2,3,4,5])
print(obj.sumRange(2,4))