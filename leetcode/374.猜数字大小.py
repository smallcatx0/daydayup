#
# @lc app=leetcode.cn id=374 lang=python3
#
# [374] 猜数字大小
#

# @lc code=start
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0

# def guess(num: int) -> int:
    

class Solution:
    def guessNumber(self, n: int) -> int:
        min,max = 0, n
        while True:
            mid = min + ((max - min) // 2)
            ans = guess(mid)
            if ans == 0:
                return mid
            elif ans < 0: # 猜大了
                max = mid - 1
            else:
                min = mid + 1
# @lc code=end

