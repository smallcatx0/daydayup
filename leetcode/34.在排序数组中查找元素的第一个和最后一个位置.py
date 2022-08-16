#
# @lc app=leetcode.cn id=34 lang=python3
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#

from time import get_clock_info
from typing import *

# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # 二分查找
        l, r = 0, len(nums) - 1
        find = -1
        while r >= l:
            i = (l + r) // 2
            if target > nums[i]:
                l = i + 1
            elif target < nums[i]:
                r = i - 1
            else:
                find = i
                break
        if find == -1:
            return [-1, -1]
        # 左右扩展
        ret = [i,i]
        while ret[0] - 1 >= 0:
            if nums[ret[0] - 1] == target:
                ret[0] -=1
            else: 
                break
        while ret[1] + 1 <= len(nums) - 1:
            if nums[ret[1] + 1] == target:
                ret[1] +=1
            else: 
                break
        return ret
# @lc code=end


if __name__ == "__main__":
    nums = [5,7,7,8,8,10]
    # nums = [1]
    # nums = []
    target = 10
    res = Solution().searchRange(nums, target)
    print(res)
