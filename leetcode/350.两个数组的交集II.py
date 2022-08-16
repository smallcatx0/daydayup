from typing import *


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ret = []
        for one in nums1:
            if one in nums2:
                ret.append(one)
                nums2.remove(one)
        return ret

    def intersect1(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ret = []
        tj = {}
        for one in nums1:
            if one in tj:
                tj[one] += 1
            else:
                tj[one] = 1
        for num in nums2:
            if num in tj and tj[num] >= 1:
                ret.append(num)
                tj[num] -= 1
        return ret

if __name__ == "__main__":
    # nums1 = [1, 2, 2, 1]
    # nums2 = [2, 2]
    nums1 = [4, 9, 9, 5]
    nums2 = [9, 4, 9, 8, 4]
    res = Solution().intersect1(nums1, nums2)
    print(res)
