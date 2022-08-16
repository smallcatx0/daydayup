#
# @lc app=leetcode.cn id=35 lang=python3
#
# [35] 搜索插入位置
#
from typing import List

# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        numLen = len(nums)
        if nums[0] > target:
            nums.insert(0, target)
            return 0
        if nums[numLen - 1] < target:
            nums.insert(numLen, target)
            return numLen
        # 查找（二分查找）
        l , r = 0, numLen
        flag = True
        while l <= r :
            mid = (r + l) // 2
            if nums[mid] < target: # 左边找
                l = mid + 1
            elif nums[mid] > target: # 右边找
                r = mid - 1
            else:
                flag = False
                break
        if flag:
            nums.insert(l, target)
            return l
        return mid
# @lc code=end
if __name__ == "__main__":
    nums, t = [5], 5
    res = Solution().searchInsert(nums,t)
    print(res, nums)