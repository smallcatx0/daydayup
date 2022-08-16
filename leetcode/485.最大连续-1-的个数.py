#
# @lc app=leetcode.cn id=485 lang=python3
#
# [485] 最大连续 1 的个数
#
from typing import *

# @lc code=start
class Solution:
    # 99.98 %(52 ms) 6.78 % (15.4 MB)
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        c,mc = 0, 0
        for x in nums:
            if x == 1:
                c += 1
            else:
                c = 0
            if c > mc:
                mc = c
        return mc
# @lc code=end

if __name__ == '__main__':
    nums = [1,0,1,1,0,1,1,1,0,1]
    res = Solution().findMaxConsecutiveOnes(nums)
    print(res)