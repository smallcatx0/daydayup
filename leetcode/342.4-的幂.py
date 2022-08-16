#
# @lc app=leetcode.cn id=342 lang=python3
#
# [342] 4的幂
#

# @lc code=start
class Solution:
    #  72.52 %(40 ms) 26.97 % (14.9 MB)
    def isPowerOfFour(self, n: int) -> bool:
        if n in (1, 4):
            return True
        while n >= 4:
            if n == 4:
                return True
            if n % 4 :
                return False
            n = n // 4
        return False
# @lc code=end


def test():
    for i in range(999):
        if not Solution().isPowerOfFour(4**i):
            print(i, 4**i)

if __name__ == '__main__':
    res = Solution().isPowerOfFour(16)
    # print(res)
    test()