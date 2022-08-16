#
# @lc app=leetcode.cn id=169 lang=python3
#
# [169] 多数元素
#
from typing import List
# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        numMaps = {}
        for one in nums:
            if one in numMaps.keys():
                numMaps[one] += 1
            else:
                numMaps[one] = 1
        maxNum = nums[0]
        for k in numMaps:
            if numMaps[k] > numMaps[maxNum]:
                maxNum = k
        return maxNum
# @lc code=end

if __name__ == "__main__":
    nums = [3,2,1,3,3]
    res = Solution().majorityElement(nums)
    print(res)