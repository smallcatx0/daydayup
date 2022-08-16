#
# @lc app=leetcode.cn id=414 lang=python3
#
# [414] 第三大的数
#
from typing import *


# @lc code=start
class Solution:
    minNum = -2 ** 32
    # 88.33% (36 ms)  91.41% (15.3 MB)
    def thirdMax(self, nums: List[int]) -> int:
        maxS = [self.minNum, self.minNum, self.minNum]
        for one in nums:
            # 打擂法
            if one in maxS:
                continue
            if one > maxS[0]:
                # 败者顺延
                maxS[2], maxS[1] = maxS[1], maxS[0]
                maxS[0] = one
            elif one > maxS[1]:
                maxS[2] = maxS[1]
                maxS[1] = one
            elif one > maxS[2]:
                maxS[2] = one
            pass
        if maxS[2] != self.minNum:
            return maxS[2]
        else:
            return maxS[0]
# @lc code=end

if __name__ == "__main__":
    nums = [2,2,2,1]
    res = Solution().thirdMax(nums)
    print(res)