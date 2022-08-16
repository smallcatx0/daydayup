#
# @lc app=leetcode.cn id=190 lang=python3
#
# [190] 颠倒二进制位
#

# @lc code=start
class Solution:
    # 74.49%(40 ms)  53.87%(14.8 MB)
    def reverseBits(self, n: int) -> int:
        i , res= 0, 0
        while n > 0:
            if(n%2):
                res += 2**(31 - i)
            n = n // 2
            i += 1
        return res
# @lc code=end


if __name__ == "__main__":
    res = Solution().reverseBits(2)
    print(res)

