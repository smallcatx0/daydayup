#
# @lc app=leetcode.cn id=367 lang=python3
#
# [367] 有效的完全平方数
#

# @lc code=start
class Solution:
    #  64.2 % (40 ms)  21.99 %(14.9 MB)
    def isPerfectSquare(self, num: int) -> bool:
        if num in (1,4, 9):
            return True
        l, r = 0, num
        while True:
            n = l + (r - l) // 2
            # 其他语言可能会数据溢出 需要将乘法转换为除法
            n_2 = n*n
            if n_2 == num:
                return True
            if n_2 > num:
                ns1_2 = (n - 1) *  (n - 1)
                if ns1_2 == num:
                    return True
                elif ns1_2 > num:
                    r = n - 1
                else:
                    return False
            else:
                na1_2 = (n + 1) *  (n + 1)
                if na1_2 == num:
                    return True
                elif na1_2 < num:
                    l = n + 1
                else:
                    return False
# @lc code=end


def test():
    for i in range(999):
        res = Solution().isPerfectSquare(i**2)
        print(i, res)
        # if (not res):
        #     print(i**2)

if __name__ == '__main__':
    i = 6
    res = Solution().isPerfectSquare(i**2)
    # print(res)
    test()
    