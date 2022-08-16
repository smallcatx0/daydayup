from typing import *


class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        numsLen = len(nums)
        if numsLen < 1:
            return 0
        i, j = 0, 0
        value = nums[i]
        minLen = numsLen + 1
        while 1:
            if value >= s:
                minLen = min(minLen, j - i + 1)
                value -= nums[i]
                i += 1
            else:
                j += 1
                if j > numsLen - 1:  # 下标越界表示找完了整个数组
                    break
                value += nums[j]

        if minLen > numsLen:
            return 0
        else:
            return minLen

if __name__ == "__main__":
    s = 7
    nums = [2, 3, 1, 2, 4, 3]  # len=6
    nums = [2]  # len=6
    res = Solution().minSubArrayLen(6, nums)
    print(res)
