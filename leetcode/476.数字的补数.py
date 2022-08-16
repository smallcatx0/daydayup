#
# @lc app=leetcode.cn id=476 lang=python3
#
# [476] 数字的补数
#

# @lc code=start
class Solution:
    def findComplement(self, num: int) -> int:
        return 2**(len(bin(num))-2)-1-num
# @lc code=end

if __name__ == "__main__":
    n = 5
    res = Solution().findComplement(n)
    print(res)