#
# @lc app=leetcode.cn id=520 lang=python3
#
# [520] 检测大写字母
#

# @lc code=start
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        upCount = 0
        if self.isUp(word[0]):
            upCount = 1
        for i in range(1, len(word)):
            # 首字符小写 不能出现大写
            if upCount == 0 and self.isUp(word[i]):
                return False
            # 前个字母为大写 则不能出现小写
            if upCount == 2 and not self.isUp(word[i]):
                return False
            if upCount == 1 and self.isUp(word[i]):
                if self.isUp(word[i - 1]):
                    upCount = 2
                else:
                    return False
        return True
    
    def isUp(self, c):
        return ord('A') <= ord(c) and ord(c) <= ord('Z')
# @lc code=end

if __name__ == "__main__":
    s = 'a'
    res = Solution().detectCapitalUse(s)
    print(res)