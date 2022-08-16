#
# @lc app=leetcode.cn id=441 lang=python3
#
# [441] 排列硬币
#

# @lc code=start
class Solution:
    def arrangeCoins(self, n: int) -> int:
        return  int((-1 +  (1 + 8*n)**0.5) / 2)
# @lc code=end

if __name__ == '__main__':
    res = Solution().arrangeCoins(9)
    print(res)
