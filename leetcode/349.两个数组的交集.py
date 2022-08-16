from typing import *


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)
        ret = set()
        for one in nums2:
            if one in set1:
                ret.add(one)
        return list(ret)


if __name__ == "__main__":
    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]
    res = Solution().intersection(nums1, nums2)
    print(res)
