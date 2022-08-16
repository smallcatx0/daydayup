#
# @lc app=leetcode.cn id=575 lang=python3
#
# [575] 分糖果
#

from typing import *

# @lc code=start
class Solution:
    # O(n) 15.3 % 164 ms
    def distributeCandies(self, candyType: List[int]) -> int:
        c,m = 0,{}
        mid = len(candyType) // 2
        for one in candyType:
            if c >= mid:
                return mid
            if one not in m.keys():
                m[one] = 1
                c += 1
        return c
# @lc code=end

if __name__ == "__main__":
    ca =  [1,2,3,4]
    res = Solution().distributeCandies(ca)
    print(res)