#
# @lc app=leetcode.cn id=16 lang=python3
#
# [16] 最接近的三数之和
#
from typing import List


# @lc code=start
class Solution:
    # O(n^2) 134ms 77%
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        ret = float('inf')  # 最接近的和
        nums.sort()
        for i in range(len(nums) - 2):
            l = i + 1
            r = len(nums) - 1
            while l < r:
                # 提前结束不可能的查找 (不知道为什么是 负优化)
                if target < ret and nums[i] + nums[l] + nums[l + 1] > ret: break
                if target > ret and nums[i] + nums[r] + nums[r - 1] < ret: break
                sumTemp = nums[i] + nums[l] + nums[r]
                if sumTemp < target:
                    l += 1
                elif sumTemp > target:
                    r -= 1
                else:
                    return target
                # print(sumTemp)
                if abs(target - sumTemp) < abs(target - ret):
                    ret = sumTemp
        return ret

# @lc code=end


if __name__ == "__main__":
    # nums, target = [-1, 2, 1, -4], 1
    nums, target = [0, 2, 1, -3], 1
    res = Solution().threeSumClosest(nums, target)
    print(res)
