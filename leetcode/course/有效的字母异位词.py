"""
给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        maps = dict()
        for c in s:
            if c in maps.keys():
                maps[c] += 1
            else :
                maps[c] = 1
        for c in t:
            if c in maps.keys():
                maps[c] -= 1
                if maps[c] == 0:
                    maps.pop(c)
        return not maps


if __name__ == "__main__":
    s = '12312309'
    t = '12312390'
    res = Solution().isAnagram(s, t)
    print(res)