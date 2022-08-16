#
# @lc app=leetcode.cn id=703 lang=python3
#
# [703] 数据流中的第 K 大元素
#
from typing import *


# @lc code=start
class KthLargest:

    _pre = []
    def __init__(self, k: int, nums: List[int]):
        MMin = -(10**5)
        self._pre = [MMin] * k
        for num in nums:
            self.add(num)

    # 5.04 %(6544 ms) 68.49 %(18.4 MB)
    def add(self, val: int) -> int:
        for i in range(len(self._pre)):
            if self._pre[i] <= val:
                self._pre.insert(i, val)
                self._pre = self._pre[0:-1]
                break
        return self._pre[-1]
        

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
# @lc code=end

if __name__ == '__main__':
    k, nums = 3, [5,2,7,9,4]
    obj = KthLargest(k, nums)
    print(obj.add(89))

