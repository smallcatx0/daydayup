#
# @lc app=leetcode.cn id=1480 lang=python3
#
# [1480] 一维数组的动态和
#
from typing import List

# @lc code=start
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        if len(nums) == 0:
            return []
        res , coun = [nums[0],], nums[0]
        for one in nums[1:]:
            coun += one
            res.append(coun)
        return res
# @lc code=end

if __name__ == "__main__":
    arr = [4]
    res = Solution().runningSum(arr)
    print(res)