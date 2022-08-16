""" 
给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。
"""
from typing import List

class Solution:
    # TimeOut
    def rotate1(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        while k > 0:
            k -= 1
            index = len(nums) - 1
            tmp = nums[index]
            while index > 0:
                nums[index] = nums[index - 1]
                index -= 1
            nums[0] = tmp

    def rotate2(self, nums: List[int], k: int) -> None:
        numsLen = len(nums)
        k = k % numsLen
        i = numsLen - k
        tmp = nums[i]
        tar = i + k - numsLen
        # print([i,tar])
        while True:
            nums[i] = nums[i - k]
            i = (numsLen + i - k ) % numsLen
            # TODO 结束的条件？
            if (i == tar) : break
        nums[tar] = tmp
    # 暴力1 
    def rotate(self, nums: List[int], k: int) -> None:
        k = k % len(nums)
        while k > 0:
            nums.insert(0, nums.pop())
            k -= 1
    
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        # [7, 8, 9, 10, 1, 2, 3, 4, 5, 6]
    k = 4
    Solution().rotate(arr, k)
    print(arr)