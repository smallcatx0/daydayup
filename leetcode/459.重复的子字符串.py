#
# @lc app=leetcode.cn id=459 lang=python3
#
# [459] 重复的子字符串
#

# @lc code=start
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        return -1 != (s+s)[1:-1].find(s)

# @lc code=end
if __name__ == '__main__':
    s = "abab"
    res = Solution().repeatedSubstringPattern(s)
    print(res)
