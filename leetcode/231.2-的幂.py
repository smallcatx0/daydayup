#
# @lc app=leetcode.cn id=231 lang=python3
#
# [231] 2的幂
#

# @lc code=start
class Solution:
    # 89.46%(36ms)  92.9% (14.6MB)
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        if n in (1, 2):
            return True
        while n != 2:
            if n % 2:
                return False
            n = n // 2
        return True
# @lc code=end

if __name__ == '__main__':
    # res = Solution().isPowerOfTwo(-16)
    # print(res)
    m = []
    for x in range(9999999):
        if Solution().isPowerOfTwo(x):
            m.append(x)
    print(m)

