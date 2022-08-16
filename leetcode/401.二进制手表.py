#
# @lc app=leetcode.cn id=401 lang=python3
#
# [401] 二进制手表
#

from typing import *

# @lc code=start
class Solution:
    def readBinaryWatch(self, num: int) -> List[str]:
        res = []
        # 直接遍历  0:00 -> 11:59   每个时间有多少1
        for h in range(0,12):
            for m in range(0,60):
                if self.count1(h) + self.count1(m) == num:
                    res.append("%d:%02d"%(h,m))
        return res

    # 计算多少个1
    def count1(self, n):
        count = 0
        while n > 0:
            n = n & (n - 1)
            count += 1
        return count

        
# @lc code=end

if __name__ == "__main__":
    # res = Solution().readBinaryWatch(2)
    res = Solution().count1(12)
    print(res)