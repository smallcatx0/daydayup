#
# @lc app=leetcode.cn id=189 lang=python3
#
# [189] 旋转数组
#
from typing import List
import time
# @lc code=start
class Solution:
    def rotate0(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        start, count = 0, 0
        numsLen = len(nums)
        k = k % numsLen
        tmp, i = nums[start], start
        while True:
            j = (i + k) % numsLen
            tmp , nums[j] = nums[j], tmp
            time.sleep(2)
            print(i, j)
            count += 1
            i = j
            if i == start and count == numsLen:
                break
            else:
                start = i + 1
                i = start
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        while k > 0:
            nums.insert(0,nums.pop())
            k -= 1

# @lc code=end
if __name__ == "__main__":
    arr = [1,2,3,4,5]
    Solution().rotate(arr,3)
    print(arr)

