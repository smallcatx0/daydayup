#
# @lc app=leetcode.cn id=118 lang=python3
#
# [118] 杨辉三角
#
from typing import List

# @lc code=start
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ret = []
        for i in range(numRows):
            line = []
            for j in range(i+1):
                line.append(self.getPos(i, j, ret))
            ret.append(line)
        return ret

    def getPos(self, i, j, ret):
        if j == 0  or i == j:
            return 1
        else:
            return ret[i-1][j-1] + ret[i-1][j]
        
# @lc code=end

if __name__ == "__main__":
    res = Solution().generate(1)
    print(res)