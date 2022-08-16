#
# @lc app=leetcode.cn id=303 lang=python3
#
# [303] 区域和检索 - 数组不可变
#

from typing import List
# @lc code=start


# 线段树 33.36 %(164 ms)  5.43 %(18.6 MB)
class NumArray:
    _segmentData = []
    _data = []
    def __init__(self, nums: List[int]):
        self._data = nums
        count = len(nums) - 1
        self._segmentData = [0] + [0,0,0,0] * count
        self.build(0, 0, count)

    def build(self, i, l, r):
        if (l == r):
            self._segmentData[i] = self._data[l]
            return 
        li = self.leftChild(i)
        ri = self.rightChild(i)
        mid = l + ((r-l) // 2)
        self.build(li, l, mid)
        self.build(ri, mid+1, r)
        self._segmentData[i] = self._segmentData[li] + self._segmentData[ri]

    def leftChild(self, i) -> int:
        return 2* i + 1

    def rightChild(self, i)-> int:
        return 2 * i + 2

    def sumRange(self, left: int, right: int) -> int:
        return self.query(0, 0, len(self._data) - 1, left, right)

    def query(self, i, l, r, ql, qr)->int:
        if l == ql and r == qr:
            return self._segmentData[i]
        mid = l + ((r-l)//2)
        left = self.leftChild(i)
        right = self.rightChild(i)
        # 查找的左边界大于了左子树的右边界 => 去右子树找
        if ql >= mid +1:
            return self.query(right, mid+1, r, ql, qr)
        elif qr <= mid:
            return self.query(left, l, mid, ql, qr)
        else:
            lv = self.query(left, l, mid, ql, mid)
            rv = self.query(right, mid+1, r, mid+1, qr)
            return lv+rv

# @lc code=end

# Your NumArray object will be instantiated and called as such:
obj = NumArray([-1])
print(obj._segmentData)
print(obj.sumRange(0,0))