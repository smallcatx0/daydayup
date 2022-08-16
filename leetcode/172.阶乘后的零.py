#
# @lc app=leetcode.cn id=172 lang=python3
#
# [172] 阶乘后的零
#

# @lc code=start
class Solution:
    def trailingZeroes(self, n: int) -> int:
        count = 0
        while (n//5 != 0):
            count += n // 5
            n = n // 5
        return count

# @lc code=end

if __name__ == "__main__":
    res = Solution().trailingZeroes(6268)
    print(res)