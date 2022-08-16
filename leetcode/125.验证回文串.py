from typing import *


class Solution:
    # O(n)
    def isPalindrome(self, s: str) -> bool:
        lp = 0
        rp = len(s) - 1
        s = s.lower()
        while(lp < rp):  # 左指针小于右指针
            if(not self.ruleIn(s[lp])):
                lp += 1
            elif(not self.ruleIn(s[rp])):
                rp -= 1
            else:
                if(s[lp] != s[rp]):
                    return False
                lp += 1
                rp -= 1
        return True

    def ruleIn(self, s: str):
        return (s >= '0' and s <= '9') or (s >= 'A' and s <= 'Z') or(s >= 'a' and s <= 'z')


if __name__ == "__main__":
    s = "A man, a plan, a canal: Panama"
    # s = "`l;`` 1o1 ??;l`"
    res = Solution().isPalindrome(s)
    # res = Solution().ruleIn('`')
    print(res)
