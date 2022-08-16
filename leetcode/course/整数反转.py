'''
给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转
'''

class Solution:
    def reverse(self, x: int) -> int:
        flag = False
        if x < 0:
            x = - x
            flag = True
        res = 0
        while x != 0:
            res = res * 10 + x % 10
            x = x // 10
            if res > 2**31 - 1:
                return 0
        if flag:
            res = - res
        return res


if __name__ == "__main__":
    x = 1534236469
    res = Solution().reverse(x)
    print(res)

