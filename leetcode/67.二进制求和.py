#
# @lc app=leetcode.cn id=67 lang=python3
#
# [67] 二进制求和
#

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a) < len(b) :
            a ,b = b ,a
        aLen, bLen = len(a), len(b)
        po , i = 0, 0
        res = []
        while i < aLen:
            if i >= bLen:
                bNum = 0
            else:
                bNum = int(b[bLen - i - 1])
            aNum = int(a[aLen - i - 1])
            sumRes = aNum + bNum + po
            res.insert(0, sumRes % 2)
            po = sumRes // 2
            i += 1
        if po != 0:
            res.insert(0, po)
        return ''.join(str(one) for one in res)

# @lc code=end

if __name__ == "__main__":
    a, b = '1110', '100'
    res = Solution().addBinary(a, b)
    print(res)