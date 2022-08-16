""" 
给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。
最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。
你可以假设除了整数 0 之外，这个整数不会以零开头。
"""
from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits) - 1
        num = 1
        while i >= 0:
            sums = digits[i] + num
            if sums < 10 :
                digits[i] = sums
                return digits
            else:
                digits[i] = sums % 10
                num = 1
            i -= 1
        digits.insert(0, num)
        return digits

if __name__ == "__main__":
    arr = [9,8,9]
    res = Solution().plusOne(arr)
    print(res)
