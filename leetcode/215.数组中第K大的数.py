from typing import *


class Solution:
    # O(nlogn)
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        return nums[len(nums) - k]

    # TODO: 利用快排的思路 优化到O(n)

if __name__ == "__main__":
    nums = [3, 2, 1, 5, 6, 4]
    k = 2
    res = Solution().findKthLargest(nums, k)
    print(res)
