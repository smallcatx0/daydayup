#
# @lc app=leetcode.cn id=58 lang=python3
#
# [58] 最后一个单词的长度
#

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        j = len(s) - 1
        flag = False
        lastLen = 0
        while j >= 0:
            if not flag and self.isAlp(s[j]):
                flag = True
            if flag :
                if not self.isAlp(s[j]):
                    return lastLen
                lastLen += 1
            j -= 1
        return lastLen

    def isAlp(self, c):
        if ord(c) >= ord('A') and ord(c) <= ord('Z'):
            return True
        if ord(c) >= ord('a') and ord(c) <= ord('z'):
            return True
        return False
# @lc code=end

if __name__ == "__main__":
    s = 'hellow world!'
    s = 'a'
    res = Solution().lengthOfLastWord(s)
    print(res)