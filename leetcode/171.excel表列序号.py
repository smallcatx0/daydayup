#
# @lc app=leetcode.cn id=171 lang=python3
#
# [171] Excel表列序号
#

# @lc code=start
class Solution:
    def titleToNumber(self, s: str) -> int:
        res, sLen = 0, len(s)
        for i in range(sLen):
            res += res * 25 + (ord(s[i]) - ord('A') + 1)
        return res
# @lc code=end

if __name__ == "__main__":
    res = Solution().titleToNumber("AB")
    print(res)