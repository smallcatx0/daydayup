""" 
给定两个数组，编写一个函数来计算它们的交集。
"""
from typing import List

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        res = []
        for one in nums1:
            for item in nums2:
                if one == item:
                    res.append(one)
                    nums2.remove(item)
                    break
        return res

    def intersect1(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
            numsLen = len(nums2)
        else :
            numsLen = len(nums2)
        res = []
        for one in nums1:
            for i in range(numsLen):
                if one == nums2[i]:
                    res.append(one)
                    nums2[i] = nums2[numsLen - 1]
                    numsLen -= 1
                    break
        return res

if __name__ == "__main__":
    arr1 = [1,2,3,2,4]
    arr2= [4,4,2,3]
    res = Solution().intersect(arr2,arr1)
    print(res)