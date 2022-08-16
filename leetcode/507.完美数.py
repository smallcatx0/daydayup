#
# @lc app=leetcode.cn id=507 lang=python3
#
# [507] 完美数
#
import math
# @lc code=start
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num <= 5:
            return False
        s = 1
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                s += (i + num // i)
        return s == num

# @lc code=end


def test():
    for num in range(10**8):
        if(Solution().checkPerfectNumber(num)):
            print(num)

if __name__ == '__main__':
    # res = Solution().checkPerfectNumber()
    test()
