#
# @lc app=leetcode.cn id=338 lang=python3
#
# [338] 比特位计数
#

# @lc code=start
from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        ret = [0] + [0] * n 
        ret[0] = 0
        for i in range(1, n+1):
            if i % 2:
                ret[i] = ret[i-1] + 1
            else:
                ret[i] = ret[i//2]
        return ret
# @lc code=end

if __name__ == '__main__':
    ret = Solution().countBits(100)
    print(ret)
