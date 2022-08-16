#
# @lc app=leetcode.cn id=136 lang=python3
#
# [136] 只出现一次的数字
#

from typing import List

# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        numSet = set()
        for num in nums:
            if num in numSet:
                numSet.remove(num)
            else:
                numSet.add(num)
        return numSet.pop()
# @lc code=end

if __name__ == "__main__":
    arr = [2,2,1,1,3,4,3]
    res = Solution().singleNumber(arr)
    print(res)