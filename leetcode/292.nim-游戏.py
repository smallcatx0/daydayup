#
# @lc app=leetcode.cn id=292 lang=python3
#
# [292] Nim 游戏
#

# @lc code=start
class Solution:
    def canWinNim(self, n: int) -> bool:
        return (n % 4) != 0
# @lc code=end


if __name__ == '__main__':
    ret = Solution().canWinNim(2)
    print(ret)