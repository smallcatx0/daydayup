#
# @lc app=leetcode.cn id=392 lang=python3
#
# [392] 判断子序列
#

# @lc code=start
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        sLen, tLen = len(s), len(t)
        i, j = 0, 0
        while i < sLen and j < tLen:
            if t[j] == s[i]:
                i += 1
            j += 1
        return i == sLen


# @lc code=end

if __name__ == "__main__":
    t = 'qqqwweeeqa'
    s = 'qwa'
    res = Solution().isSubsequence(s, t)
    print(res)