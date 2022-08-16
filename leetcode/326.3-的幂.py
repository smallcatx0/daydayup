#
# @lc app=leetcode.cn id=326 lang=python3
#
# [326] 3的幂
#

# @lc code=start
class Solution:
    #  89.2%(80ms) 15.02 %(14.9 MB)
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        if n in (1, 3):
            return True
        while n != 3:
            if n % 3: 
                return False
            n = n // 3
        return True
# @lc code=end

