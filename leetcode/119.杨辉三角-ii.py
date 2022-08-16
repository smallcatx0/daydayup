#
# @lc app=leetcode.cn id=119 lang=python3
#
# [119] 杨辉三角 II
#

from typing import List

# @lc code=start
class Solution:
    _cache = {}
    count = 0
    def getRow(self, rowIndex: int) -> List[int]:
        ret = []
        # TODO 只算一半
        for i in range(rowIndex + 1):
            ret.append(self.getPos(i, rowIndex))
        return ret
    
    def getPos(self, i, j):
        if i == 0  or i == j:
            return 1
        # 查缓存
        key1 = "%d,%d"%(i, j)
        if key1 in self._cache.keys():
            return self._cache[key1]
        # 对称查询
        key2 = "%d,%d"%(j - i, j)
        if key2 in self._cache.keys():
            return self._cache[key2]
        # 缓存
        self._cache[key1] = self.getPos(i-1, j-1) + self.getPos(i, j - 1)
        self.count += 1
        return self._cache[key1]
# @lc code=end
if __name__ == "__main__":
    # res = Solution().getRow(50)
    sl = Solution()
    res = sl.getRow(50)
    print(sl.count)