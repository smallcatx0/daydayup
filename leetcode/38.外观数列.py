#
# @lc app=leetcode.cn id=38 lang=python3
#
# [38] 外观数列
#

# @lc code=start
class Solution:
    def countAndSay(self, n: int) -> str:
        res, i = '1', 1
        while i < n:
            res = self.say(res)
            i += 1
        return res
    def say(self, strs):
        num = strs[0]
        count = 1
        res = ''
        for c in strs[1:]:
            if c == num:
                count += 1
            else:
                res += "%s%s"%(count,num)
                num = c
                count = 1
        return res + "%s%s"%(count, num)
# @lc code=end

if __name__ == "__main__":
    n = 4
    res = Solution().countAndSay(n)
    print(res)