from typing import *


class Solution:
    # O(nlogn)
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(0, len(numbers)):
            remain = target - numbers[i]
            if(remain < numbers[i]):
                continue
            j = self.binarySearch(numbers[i+1:], remain)  # 在[i+1..n]里找
            if j != -1:
                return [i + 1, i + j + 2]

    # time out
    def twoSum1(self, numbers: List[int], target: int) -> List[int]:
        for i in range(0, len(numbers)):
            remain = target - numbers[i]
            if(remain < numbers[i]):
                continue
            try:
                j = numbers[i+1:].index(remain)
                return [i + 1, i + j + 2]
            except Exception:
                pass

    # O(n)
    def twoSum2(self, numbers: List[int], target: int) -> List[int]:
        '''对撞指针
        '''
        lp = 0
        rp = len(numbers) - 1
        while lp < rp:
            if numbers[lp] + numbers[rp] == target:
                return [lp + 1, rp + 1]
            elif numbers[lp] + numbers[rp] > target:
                rp -= 1
            else:
                lp += 1

    def binarySearch(self, nums: List[int], target):
        lp = 0
        rp = len(nums)-1  # [lp..rp] 区间之间寻找
        while lp <= rp:   # [lp..rp] lp==rp 时候区间任有元素
            mid = (lp + rp) // 2
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:  # 前半截不包含mid [lp..mid-1]
                rp = mid - 1
            else:                     # 后半截不包含mid [mid+1..rp]
                lp = mid + 1
        return -1


if __name__ == "__main__":
    numbers = [1, 1, 2, 4, 7, 11, 15]
    target = 9
    res = Solution().twoSum2(numbers, target)
    # res = Solution().binarySerch(numbers[1:], 7)
    print(res)
