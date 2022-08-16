#
# @lc app=leetcode.cn id=455 lang=python3
#
# [455] 分发饼干
#
from typing import *

# @lc code=start
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort(reverse=True)
        s.sort(reverse=True)
        mz = 0
        for c in g:
            # 找到 >=c 的最小值
            i = self.minGt(c, s)
            if i != -1:
                mz += 1
                del s[i]
        return mz
            # print(i, c, s) 
    # 5.01 %(1052 ms)
    def minGt(self, c, s):
        for i in range(len(s)):
            if s[i] >= c:
                return i
        return -1
    # TODO: 二分查找法 找到最小满足
    def minGt2(self, c, s):
        if s[-1] < c:
            return -1
        l,r = 0, len(s)-1
        while l <= r:
            mid = l + (r - l) // 2
            if s[mid] >= c:
                if s[mid + 1] <= c:
                    return mid
                else:
                    l = mid + 1
            else:
                if s[mid - 1] >= c:
                    return mid + 1
                else:
                    r = mid - 1
        return -1
# @lc code=end


if __name__ == "__main__":
    g ,s = [1,2], [1,2,3,4,5]
    # res = Solution().findContentChildren(g,s)
    res = Solution().minGt2(2, s)
    print(res)

# %%
s = [1,2,3]
s.sort(reverse=True)
s[-1]
# %%
