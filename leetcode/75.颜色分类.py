from typing import *


class Solution:

    def sortColors(self, nums: List[int]) -> None:
        nums.sort()

    def sortColors1(self, nums: List[int]) -> None:
        """统计排序法
        """
        stat = [0, 0, 0]
        for x in nums:
            assert x >= 0 and x <= 2
            stat[x] += 1
        index = 0
        for i in range(0, len(stat)):
            for t in range(0, stat[i]):
                nums[index] = i
                index += 1

    def sortColors2(self, nums: List[int]) -> None:
        zero = -1        # [0..zero] == 0
        two = len(nums)  # [two..n] == 2
        i = 0            # [i..two) == 1
        while (i < two):
            if nums[i] == 1:
                i += 1
            elif nums[i] == 2:
                two -= 1
                nums[i], nums[two] = nums[two], nums[i]
            else:
                assert nums[i] == 0
                zero += 1
                nums[zero], nums[i] = nums[i], nums[zero]
                i += 1


if __name__ == "__main__":
    nums = [2, 0, 2, 1, 1, 0]
    Solution().sortColors2(nums)
    print(nums)
