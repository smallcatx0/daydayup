'''
给定一个整数数组和一个整数 k，判断数组中是否存在两个不同的索引 i 和 j，使得 nums [i] = nums [j]，并且 i 和 j 的差的绝对值最大为 k。

链接：https://leetcode-cn.com/problems/contains-duplicate-ii
'''
from typing import *


class Solution:
    # O(n) 132ms 71%
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if len(nums) == 0 or k == 0:
            return False
        l, r = 0, 0
        searchSet = set((nums[0],))
        while r <= k - 2 and r < len(nums) - 1:
            if nums[r + 1] in searchSet:
                return True
            r += 1
            searchSet.add(nums[r])
        print(l, r, searchSet)
        while r < len(nums) - 1:
            if nums[r + 1] in searchSet:
                return True
            else:
                r += 1
                searchSet.add(nums[r])
                searchSet.remove(nums[l])
                l += 1
        return False

    # O(n) 128ms 75%
    def containsNearbyDuplicate1(self, nums: List[int], k: int) -> bool:
        if len(nums) == 0 or k == 0: return False
        searchSet = set((nums[0],))
        for i in range(1, len(nums)):
            if nums[i] in searchSet:
                return True
            searchSet.add(nums[i])
            if len(searchSet) >= k + 1:
                searchSet.remove(nums[i-k])
        return False


if __name__ == "__main__":
    nums, k = [1, 2, 3, 1], 3
    # nums, k = [0, 1, 2, 3, 1], 3
    nums, k = [1, 2, 3, 1, 2, 3], 2
    # nums, k = [1, 0, 1, 1], 1
    # nums, k = [2, 2], 3
    # nums, k = [1, 2, 3, 1, 1, 2, 3], 0
    res = Solution().containsNearbyDuplicate1(nums, k)
    print(res)
