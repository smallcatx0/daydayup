
from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # 左边 *2 + i = sum
        s = sum(nums)
        ls2 = 0
        for i in range(len(nums)):
            if ls2 + nums[i] == s:
                return i
            ls2 += nums[i]*2
            i += 1
        return -1
        


if __name__ == '__main__':
    nums = [-2,1,-1]
    # nums = [-1,-1,-1,-1,-1,0]
    ret = Solution().pivotIndex(nums)
    print(ret)