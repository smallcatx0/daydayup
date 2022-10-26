
from copy import copy
from typing import Dict, List

class Solution:
    def s2m(self, s)->Dict:
        h,i = {}, 0
        while s[i:]:
            c = s[i].lower()
            i += 1
            # 判断 c 是否字母
            if c > 'z' or c < 'a':
                continue
            if c in h:
                h[c] += 1
            else:
                h[c] = 1
        return h
    def mit(self, w:str, h:Dict) -> bool:
        h,i = copy(h),0
        while w[i:]:
            c = w[i].lower()
            i += 1
            if c in h:
                h[c] -= 1
                if h[c] <= 0:
                    del(h[c])
                if len(h) == 0:
                    return True
        return False

    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        # world排序
        words = sorted(words, key=len)
        h = self.s2m(licensePlate)
        # print(h)
        for w in words:
            if self.mit(w, h):
                return w
        return

if __name__ == '__main__':
    s = "1s3 PSt"
    words = ["step", "steps", "stripe", "stepple"]
    ret = Solution().shortestCompletingWord(s, words)
    print(ret)