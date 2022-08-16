#
# @lc app=leetcode.cn id=1331 lang=python3
#
# [1331] 数组序号转换
#

from typing import *

# @lc code=start
class Solution:
    # 72.94 %(364 ms)
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        smp,al = {}, len(arr)
        newArr = list(set(arr))
        newArr.sort()
        for i in range(len(newArr)):
            smp[newArr[i]] = i + 1
        for i in range(al):
            arr[i] = smp[arr[i]]
        return arr
# @lc code=end

if __name__ == "__main__":
    arr = [40,10,20,10,30]
    res = Solution().arrayRankTransform(arr)
    print(res)