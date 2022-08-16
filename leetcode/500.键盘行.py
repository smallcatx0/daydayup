#
# @lc app=leetcode.cn id=500 lang=python3
#
# [500] 键盘行
#

from typing import *

# @lc code=start
class Solution:
    kb = {
        "q":1, "w":1, "e":1, "r":1, "t":1, "y":1, "u":1, "i":1, "o":1, "p":1,
        "a":2, "s":2, "d":2, "f":2, "g":2, "h":2, "j":2, "k":2, "l":2,
        "z":3, "x":3, "c":3, "v":3, "b":3, "n":3, "m":3,
    }
    # 11.91 %(48ms)
    def findWords(self, words: List[str]) -> List[str]:
        res = []
        for word in words:
            if len(word) == 0:
                continue
            h,bk = self.kb[word[0].lower()], False
            for c in word[1:]:
                if h != self.kb[c.lower()]:
                    bk = True
                    continue
            if not bk:
                res.append(word)
        return res 

# @lc code=end


if __name__ == "__main__":
    words = ["Hello","Alaska","Dad","Peace", ""]
    res = Solution().findWords(words)
    print(res)