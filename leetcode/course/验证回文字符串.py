""" 
给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。
"""
class Solution:
    def isPalindrome(self, s: str) -> bool:
        i,j = 0, len(s) - 1
        while i < j:
            if not self.isAva(s[i]) :
                i += 1
            elif not self.isAva(s[j]):
                j -= 1
            else:
                if s[i].upper() == s[j].upper():
                    i += 1
                    j -= 1
                else : 
                    return False
        return True

    def isAva(self, c:chr) -> bool:
        return c.isalnum()

if __name__ == "__main__":
    s = "123,,,,433,,,21"
    res = Solution().isPalindrome(s)
    print(res)