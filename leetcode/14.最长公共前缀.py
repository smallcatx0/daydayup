#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#
from typing import List

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ''
        i = 0
        res = ''
        while True:
            tempChar = ''
            for one in strs:
                if len(one) <= i:
                    return res
                if tempChar == '':
                    tempChar = one[i]
                if tempChar != one[i]:
                    return res
            res += tempChar
            i += 1

# @lc code=end

if __name__ == "__main__":
    strs = ["flower", "", "floiu"]
    strs = []
    res = Solution().longestCommonPrefix(strs)
    print(res)