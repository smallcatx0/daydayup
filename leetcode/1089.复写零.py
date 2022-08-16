#
# @lc app=leetcode.cn id=1089 lang=python3
#
# [1089] 复写零
#

# @lc code=start
from typing import List


class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        i, n = 0, len(arr)
        while i < n:
            if arr[i] == 0:
                arr.insert(i, 0)
                arr.pop()
                i+=2
            else:
                i+=1

# @lc code=end

if __name__ == '__main__':
    arr = [1,0,2,3,0,4,5,0]
    Solution().duplicateZeros(arr)
    print(arr)