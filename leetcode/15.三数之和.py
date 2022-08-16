#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#
from typing import List

# @lc code=start

class Solution:
    # O(n^2)
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ret = []
        serchMap = {}
        # 关于去重--莫得思路
        for i in range(0, len(nums)):
            for j in range(0, len(nums)):
                if nums[j] in serchMap and serchMap[nums[j]] is not None:
                    ret.append((j, serchMap[nums[j]][0], serchMap[nums[j]][1]))
                    serchMap[nums[j]] = None
                else:
                    serchMap[0 - nums[i] - nums[j]] = (nums[i], nums[j])
        return ret

    # 先排序 再查找
    # O(n^2) 1524ms 35.58%
    def threeSum2(self, nums: List[int]) -> List[List[int]]:
        ret = []
        nums.sort()
        i = 0
        for i in range(len(nums) - 2):
            if i != 0 and nums[i] == nums[i - 1]: continue  # 跳过重复
            l = i + 1
            r = len(nums) - 1
            while l < r:
                # 提前淘汰掉不可能的情况
                if nums[i] + nums[r] + nums[r - 1] < 0 or nums[i] + nums[i + 1] + nums[i + 2] > 0:
                    break
                tsum = nums[i] + nums[l] + nums[r]
                if tsum > 0:
                    r -= 1
                elif tsum < 0:
                    l += 1
                else:
                    ret.append((nums[i], nums[l], nums[r]))
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]: l += 1
                    while l < r and nums[r] == nums[r + 1]: r -= 1

        return ret

# @lc code=end


if __name__ == "__main__":
    nums = [0, 0, 0, 0]
    # nums = [-1, 0, 1, 2, -1, -4]
    nums = [-2, 0, 1, 1, 2]
    # res = Solution().threeSum(nums)
    res = Solution().threeSum2(nums)
    print(res)
