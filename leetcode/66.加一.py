#
# @lc app=leetcode.cn id=66 lang=python3
#
# [66] 加一
#

from typing import List
# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        j = len(digits) - 1
        num = digits[j] + 1
        pos = num // 10
        digits[j] = num % 10
        j -= 1
        while pos != 0 and j >= 0:
            num = digits[j] + pos
            pos = num // 10
            digits[j] = num % 10
            j -= 1
        if pos != 0:
            digits.insert(0,pos)
        return digits

# @lc code=end

if __name__ == "__main__":
    nums = [1,9,9]
    res = Solution().plusOne(nums)
    print(res)