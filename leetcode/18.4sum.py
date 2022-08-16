'''
给定一个包含 n 个整数的数组 nums 和一个目标值 target，判断 nums 中是否存在四个元素 a，b，c 和 d ，使得 a + b + c + d 的值与 target 相等？找出所有满足条件且不重复的四元组。

链接：https://leetcode-cn.com/problems/4sum
'''
from typing import *


class Solution:

    def addRet(self, now, mayAns):
        for one in mayAns:
            if now[0] in one or now[1] in one:
                continue
            tempList = [self.nums[one[0]], self.nums[one[1]], self.nums[now[0]], self.nums[now[1]]]
            tempList.sort()
            Key = ''.join(str(s) for s in tempList)
            self.ret[Key] = tempList

    # O(n^2) 232 ms 77%
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.ret = {}
        self.nums = nums
        searchMap = {}
        for i in range(len(nums)):
            for j in range((len(nums))):
                if i == j:
                    continue
                tmpSum = nums[i] + nums[j]
                if target - tmpSum in searchMap:
                    self.addRet((i, j), searchMap[target - tmpSum])
                elif tmpSum in searchMap:
                    searchMap[tmpSum].append((i, j))
                else:
                    searchMap[tmpSum] = [(i, j)]
        print(searchMap)
        return list(self.ret.values())

    # O(n^2) 200ms 77%
    def fourSum1(self, nums: List[int], target: int) -> List[List[int]]:
        ret = {}
        searchMap = {}
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j:
                    continue
                tmpSum = nums[i] + nums[j]
                if target - tmpSum in searchMap:
                    for one in searchMap[target - tmpSum]:
                        if i in one or j in one:
                            continue
                        tmpList = [nums[i], nums[j], nums[one[0]], nums[one[1]]]
                        tmpList.sort()
                        tmpKey = ''.join(str(s) for s in tmpList)
                        ret[tmpKey] = tmpList  # 结果集去重
                elif tmpSum in searchMap:
                    if i < j:
                        searchMap[tmpSum].append((i, j))
                else:
                    searchMap[tmpSum] = [(i, j)]
        return list(ret.values())


if __name__ == "__main__":
    nums, target = [1, 0, -1, 0, -2, 2], 0
    nums, target = [2, -4, -5, -2, -3, -5, 0, 4, -2], -14
    res = Solution().fourSum1(nums, target)
    # res = Solution().fourSum(nums, target)
    print(res)
