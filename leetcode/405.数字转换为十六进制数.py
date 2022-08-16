#
# @lc app=leetcode.cn id=405 lang=python3
#
# [405] 数字转换为十六进制数
#

# @lc code=start
class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return '0'
        h = '0123456789abcdef'
        res = ""
        while num != 0 and len(res) < 8:
            res = h[num & 0x0f] + res
            num = num >> 4
        return res

# @lc code=end


if __name__ == '__main__':
    res = Solution().toHex(-31)
    print(res)
