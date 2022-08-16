#
# @lc app=leetcode.cn id=728 lang=python3
#
# [728] 自除数
#

from typing import *

# @lc code=start
class Solution:
    # 100 %(32 ms)
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        res = []
        if left <= 12:
            res += [i for i in range(left, min(13, right))]
            res.remove(10)
        if left<=15 and right >= 15:
            res.append(15)
        if left <=22 and right >= 22:
            res.append(22)
        for num in range(max(left, 23), right + 1):
            if self.isZ(num):
                res.append(num)
        return res
    
    def isZ(self, num):
        num1 = num
        while num != 0:
            w = num % 10
            num = num // 10
            if w == 0:
                return False
            if num1 % w != 0:
                return False
        return True
# @lc code=end

if __name__ == "__main__":
    l,r = 1,85
    res = Solution().selfDividingNumbers(l,r)
    print(res)