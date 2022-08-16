#
# @lc app=leetcode.cn id=415 lang=python3
#
# [415] 字符串相加
#

# @lc code=start
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        l1, l2 = len(num1), len(num2)
        if(l1==0 and l2 == 0):
            return '0'
        res = ''
        i, j, m = 0, 0 ,0
        while i < l1 or j < l2:
            a, b = 0,0
            if i < l1:
                a = num1[l1 - i - 1]
                i += 1
            if j < l2:
                b = num2[l2 - j - 1]
                j += 1
            s = int(a) + int(b) + m
            m = s // 10
            res = str(s % 10) + res
        if m != 0:
            res = str(m) + res
        return res
# @lc code=end

if __name__ == "__main__":
    # res = Solution().readBinaryWatch(2)
    res = Solution().addStrings('72', '34')
    print(res)