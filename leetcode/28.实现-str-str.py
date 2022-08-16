#
# @lc app=leetcode.cn id=28 lang=python3
#
# [28] 实现 strStr()
#

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        sLen = len(haystack)
        tLen = len(needle)
        if tLen == 0:
            return 0
        if tLen > sLen:
            return -1
        for i in range(sLen - tLen + 1):
            if haystack[i: i + tLen] == needle:
                return i
        return -1
# @lc code=end

if __name__ == "__main__":
    s = "hello",
    t = "ll"
