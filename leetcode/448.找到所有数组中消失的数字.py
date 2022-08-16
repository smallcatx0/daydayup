#
# @lc app=leetcode.cn id=448 lang=python3
#
# [448] 找到所有数组中消失的数字
#

from typing import *

# @lc code=start
class Solution:
    # 84.18%(144ms)  14.57%(24.7MB)
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        tomapp = {}
        for i in range(1, len(nums) + 1):
            tomapp[i] = 1
        for one in nums:
            if one in tomapp.keys():
                del tomapp[one]
        return list(tomapp.keys())
# @lc code=end


if __name__ == "__main__":
    # arr = [4,3,2,7,8,2,3,1]
    arr = [4,1]
    res = Solution().findDisappearedNumbers(arr)
    print(res)