from typing import *


class Solution:
    # 时间复杂度 O(n)
    # 空间复杂度 O(n)
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        noZeroesArr = []
        for x in nums:
            if x != 0:
                noZeroesArr.append(x)
        for i in range(0, len(noZeroesArr)):
            nums[i] = noZeroesArr[i]
        for i in range(len(noZeroesArr), len(nums)):
            nums[i] = 0

    # 时间复杂度 O(n)
    # 空间复杂度 O(1)
    def moveZeroes1(self, nums: List[int]) -> None:
        k = 0  # [0,k)保存这个数值的所有非0元素
        for x in nums:
            if x != 0:
                nums[k] = x
                k += 1
        for i in range(k, len(nums)):
            nums[i] = 0

    # 时间复杂度 O(n)
    # 空间复杂度 O(1)
    def moveZeroes2(self, nums: List[int]) -> None:
        k = 0  # [0,k)保存这个数值的所有非0元素
        for i in range(0, len(nums)):
            if nums[i] != 0:
                if i == k:
                    k += 1
                else:
                    nums[k] = nums[i]
                    nums[i] = 0
                    k += 1

if __name__ == "__main__":
    listdata = [0, 1, 0, 3, 9, 0]
    Solution().moveZeroes2(listdata)
    print(listdata)
