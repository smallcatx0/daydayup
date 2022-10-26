
from typing import List


class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return -1
        if len(nums) ==1:
            return 0
        i0,i1 = 0,1
        if nums[1] > nums[0]:
            i0, i1 = 1,0
        for i in range(2, len(nums)):
            if nums[i] >= nums[i0]:
                i1,i0 = i0,i
            elif nums[i] >= nums[i1]:
                i1 = i
        print(nums[i0], nums[i1], nums[i0] >= 2*nums[i1])
        if nums[i0] >= 2*nums[i1]:
            return i0
        return -1
        

if __name__=='__main__':
    nums = [1,2,3,9,4]
    nums = [0,0,3,2]
    ret = Solution().dominantIndex(nums)
    print(ret)