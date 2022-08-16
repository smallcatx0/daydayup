#
# @lc app=leetcode.cn id=88 lang=python3
#
# [88] 合并两个有序数组
#
from typing import List

# @lc code=start
class Solution:
    # o((m+n)log(m+n)) + O(n) = O(NlogN) [N = m+n]
    def merge1(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """暴力解法
        """
        for i in range(0, n):  # O(n)
            nums1[m + i] = nums2[i]
        nums1.sort()  # O((m+n)log(m+n))
        

    # o(N) N=m+n
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """数据归并，从末尾扫不用辅助空间
        """
        last = m + n - 1
        m -= 1
        n -= 1
        while m >= 0 and n >= 0:
            if nums1[m] >= nums2[n]:
                nums1[last] = nums1[m]
                last -= 1
                m -= 1
            else:
                nums1[last] = nums2[n]
                last -= 1
                n -= 1
        while n >= 0:
            nums1[last] = nums2[n]
            last -= 1
            n -= 1

# @lc code=end


if __name__ == "__main__":
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    Solution().merge1(nums1, m, nums2, n)
    print(nums1)
