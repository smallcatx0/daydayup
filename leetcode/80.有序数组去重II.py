from typing import *


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        numsLen = len(nums)
        if numsLen <= 2:
            return numsLen
        k = 0  # [0 ~ k] 保存符合要求的数据
        times = 1  # 重复次数
        for i in range(1, numsLen):
            if nums[i] == nums[k]:
                times += 1
                if times <= 2:
                    k += 1
                    nums[k] = nums[i]
            else:
                k += 1
                nums[k] = nums[i]
                times = 1
        return k+1


if __name__ == "__main__":
    nums = [0, 0, 0, 1, 1, 3, 3, 3, 7, 7]
    res = Solution().removeDuplicates(nums)
    print(nums[:res])
