#
# @lc app=leetcode.cn id=263 lang=python3
#
# [263] 丑数
#

# @lc code=start
class Solution:
    def isUgly(self, num: int) -> bool:
        if num == 0:
            return False
        while num != 1:
            if (num % 2) == 0:
                num = num // 2
            elif (num % 3) == 0:
                num = num // 3
            elif (num % 5) == 0:
                num = num // 5
            else:
                return False
        return True
# @lc code=end

if __name__ == "__main__":
    num = 1
    res = Solution().isUgly(num)
    print(res)