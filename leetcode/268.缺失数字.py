#
# @lc app=leetcode.cn id=268 lang=python3
#
# [268] 缺失数字
#

from typing import List

# @lc code=start
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        s1, s2 = 0, 0
        for i in range(len(nums)):
            s1 += i
            s2 += nums[i]
        return (s1 + i + 1) - s2
# @lc code=end

if __name__ == "__main__":
    arr = [0,1,2,4]
    res = Solution().missingNumber(arr)
    print(res)
