from typing import *
import time
import Util
import copy


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for i in range(0, len(nums)):
            if nums[i] != val:
                if i != k:
                    nums[k] = nums[i]
                k += 1
        return k

    def removeElement1(self, nums: List[int], val: int) -> int:
        k = 0
        i = 0
        numsLen = len(nums)
        while i < numsLen:
            if nums[i] != val:
                if i != k:
                    nums[k] = nums[i]
                k += 1
            i += 1
        return k


if __name__ == "__main__":
    length = 10**6
    scope = 50
    nums = Util.randomArray(length, scope)
    nums1 = copy.copy(nums)
    print("test array length is %d random in [0 ~ %d]" % (length, scope))
    st = time.time()
    res = Solution().removeElement(nums, 40)
    ed = time.time()
    print("A results= %d cost %fs" % (res, ed - st))
    st = time.time()
    res = Solution().removeElement1(nums1, 40)
    ed = time.time()
    print("B results= %d cost %fs" % (res, ed - st))
