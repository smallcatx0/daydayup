#
# @lc app=leetcode.cn id=704 lang=python3
#
# [704] 二分查找
#
from typing import *


# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if(nums[mid] == target):
                return mid
            elif(target > nums[mid]):
                l = mid + 1
            else:
                r = mid - 1
        return -1
# @lc code=end

if __name__ == '__main__':
    nums = [5]
    target = 5
    res = Solution().search(nums, target)
    print(res)