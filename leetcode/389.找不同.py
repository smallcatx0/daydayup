#
# @lc app=leetcode.cn id=389 lang=python3
#
# [389] 找不同
#

# @lc code=start
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        charMap  = {}
        for c in s:
            if c in charMap.keys():
                charMap[c] += 1
            else:
                charMap[c] = 1
        for c in t:
            if c not in charMap.keys():
                return c
            charMap[c] -= 1
            if charMap[c] == 0:
                del charMap[c]
        return ''
# @lc code=end

if __name__ == "__main__":
    s, t = 'abcd', 'abcde'
    res = Solution().findTheDifference(s, t)
    print(res)