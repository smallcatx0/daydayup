#
# @lc app=leetcode.cn id=228 lang=python3
#
# [228] 汇总区间
#
from typing import *

# @lc code=start
class Solution:
    # 8.19%(56ms)  85.58% (14.7MB)
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return [str(nums[0])]
        st, ls = nums[0], 0
        res = []
        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] == 1:
                ls += 1
            else:
                if(ls == 0):
                    res.append("%d"%st)
                else:
                    res.append("%d->%d"%(st, st+ls))
                st = nums[i]
                ls = 0
        if(ls == 0):
            res.append("%d"%st)
        else:
            res.append("%d->%d"%(st, st+ls))
        return res
# @lc code=end


if __name__ == '__main__':
    arr = [1,3,5,6,7, 9]
    res = Solution().summaryRanges(arr)
    print(res)