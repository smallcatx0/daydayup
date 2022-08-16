#
# @lc app=leetcode.cn id=12 lang=python3
#
# [12] 整数转罗马数字
#

# @lc code=start
class Solution:
    ONE = ["", "I", "II", "III", "IV", 'V', 'VI','VII' , 'VIII', 'IX']
    TEN = ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
    HUNDER = ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']
    THOU = ['', 'M', 'MM', 'MMM']
    def intToRoman(self, num: int) -> str:
        return self.THOU[num // 1000] + \
            self.HUNDER[num % 1000 // 100] + \
            self.TEN[num % 100 // 10] + \
            self.ONE[num % 10]
# @lc code=end

if __name__=='__main__':
    res = Solution().intToRoman(9)
    print(res)