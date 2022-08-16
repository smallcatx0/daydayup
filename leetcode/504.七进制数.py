#
# @lc app=leetcode.cn id=504 lang=python3
#
# [504] 七进制数
#

# @lc code=start
class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return '0'
        val = abs(num)
        ret = []
        while val > 0:
            ret.append(val % 7)
            val = val // 7
        return ('-' if num < 0 else '') + ''.join([str(x) for x in ret[len(ret)::-1]])
# @lc code=end

if __name__ == "__main__":
    res = Solution().convertToBase7(3)
    print(res)



    