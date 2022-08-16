#
# @lc app=leetcode.cn id=204 lang=python3
#
# [204] 计数质数
#
# @lc code=start
import math
class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 3:
            return 0
        m = [1]*n
        m[0], m[1] = 0,0
        # 从第一个质数开始 将他的倍数全为非质数
        for i in range(2, int(n**0.5) + 1):
            if m[i] == 1:
                m[i*i:n:i] = [0] * len(m[i*i:n:i])
        return sum(m)

    # timeout
    def isPrime(self, num: int)-> bool:
        # 跳过些些较小的数
        if num in (2, 3, 5, 7, 11):
            return True
        # 不为6i-1 6i+1 的数一定不是质数
        if (num % 6 != 1) and (num % 6 != 5):
            return False
        i,tmp = 5, math.sqrt(num)
        while i <= tmp:
            if num % i == 0 or num % (i+2) == 0:
                return False
            i += 6
        return True
# @lc code=end

if __name__ == '__main__':
    n = 100
    res = Solution().countPrimes(n)
    # res = Solution().isPrime(25)
    print(res)