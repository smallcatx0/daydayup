#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子序和
#

from typing import List

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        pre, maxRes = 0, nums[0]
        for one in nums:
            pre = max(pre + one, one)
            maxRes = max(maxRes, pre)
        return maxRes
# @lc code=end

if __name__ == "__main__":
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    nums = [1,2,-1,-2,2,1,-2,1,4,-5,4]
    res = Solution().maxSubArray(nums)
    # res = Solution().moveWhere(3,8,nums)
    print(res)