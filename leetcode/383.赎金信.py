#
# @lc app=leetcode.cn id=383 lang=python3
#
# [383] 赎金信
#

# @lc code=start
class Solution:
    # 24.43 %(92ms) 80.76 %(15 MB)
    def canConstruct1(self, ransomNote: str, magazine: str) -> bool:
        mmap = {}
        for c in magazine:
            if c in mmap.keys():
                mmap[c] += 1
            else:
                mmap[c] = 1
        for c in ransomNote:
            if c in mmap.keys() and mmap[c] > 0:
                mmap[c] -= 1
            else:
                return False
        return True

    # 93.43 %(48 ms) 
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for c in ransomNote:
            if c in magazine:
                magazine = magazine.replace(c, '', 1)
            else:
                return False
        return True

# @lc code=end

if __name__ == '__main__':
    q,s = 'aa', 'ab'
    res = Solution().canConstruct(q,s)
    print(res)

