#
# @lc app=leetcode.cn id=4 lang=python3
#
# [4] 寻找两个正序数组的中位数
#

# @lc code=start
from typing import *


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l1, l2 = len(nums1), len(nums2)
        isOdd = (l1 + l2) % 2
        midIndex =(l1 + l2 + 1) // 2
        curr = pre = 0
        Mmin = -10**7
        while midIndex >= 0:
            l1max = l2max = Mmin
            if l1 > 0:
                l1max = nums1[l1 - 1]
            if l2 > 0:
                l2max = nums2[l2 - 1]
            if l2max > l1max:
                pre = curr
                curr = l2max
                l2 -=1
                midIndex -= 1
            else:
                pre = curr
                curr = l1max
                l1 -= 1
                midIndex -= 1
        if isOdd:
            return pre
        else:
            return (curr + pre) / 2
# @lc code=end


if __name__ == "__main__":
    num1 = [3]
    num2 = [-2, -1]
    res = Solution().findMedianSortedArrays(num1, num2)
    print(res)