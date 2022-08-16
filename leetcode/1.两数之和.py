#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#
from typing import List


# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        serchSet = {}
        for i in range(0, len(nums)):
            num = target - nums[i]
            if num in (serchSet):
                return [serchSet[num], i]
            else:
                serchSet[nums[i]] = i

# @lc code=end


if __name__ == "__main__":
    nums = [2, 11, 7, 15]
    target = 9
    res = Solution().twoSum(nums, target)
    print(res)
