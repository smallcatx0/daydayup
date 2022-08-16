#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#

# @lc code=start
from typing import List


class Solution:
    # 28 ms(98.33 %)  15 MB(78.27 %)
    def generateParenthesis(self, n: int) -> List[str]:
        res = self.gent([], n, n)
        return res

    def gent(self, s:List , l , r) -> List[str]:
        res = []
        if l == 0 or r == 0:
            # 补全
            res.append(''.join(s + [')'] *r))
            return res
        if l == r:
            res += self.gent(s + ['('], l-1, r)
        else:
            if l > 0:
                res += self.gent(s + ['('], l-1, r)
            res += self.gent(s + [')'], l, r-1)
        return res

# @lc code=end

if __name__ == '__main__':
    res = Solution().generateParenthesis(3)
    print(res)
    print(len(res))