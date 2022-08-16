#
# @lc app=leetcode.cn id=168 lang=python3
#
# [168] Excel表列名称
#

# @lc code=start
class Solution:
    def convertToTitle(self, n: int) -> str:
        return self.cv(n - 1)

    def cv(self, n):
        if n < 26:
            return chr(ord('A') + n)
        else:
            return self.cv((n // 26) - 1) + self.cv(n % 26)
# @lc code=end

if __name__ == "__main__":
    res = Solution().convertToTitle(27)
    print(res)
