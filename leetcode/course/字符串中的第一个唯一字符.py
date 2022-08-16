""" 
给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。
"""


class Solution:
    def firstUniqChar(self, s: str) -> int:
        maps = dict()
        for c in s:
            if c in maps.keys():
                maps[c] += 1
            else:
                maps[c]  = 1
        for i in range(len(s)):
            if maps[s[i]] == 1:
                return i
        return -1


if __name__ == "__main__":
    s = "heellh2"
    res = Solution().firstUniqChar(s)
    print(res)