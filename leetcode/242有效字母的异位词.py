class Solution:
    # O(n)
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        tMap = [0] * 26
        sMap = [0] * 26
        for aChar in t:
            tMap[ord(aChar) - ord('a')] += 1
        for aChar in s:
            sMap[ord(aChar) - ord('a')] += 1
        for i in range(0, 26):
            if tMap[i] != sMap[i]:
                return False
        return True

    # O(n) 比上一个差
    def isAnagram1(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        tMap = [0] * 26
        for aChar in t:
            tMap[ord(aChar) - ord('a')] += 1
        for aChar in s:
            if tMap[ord(aChar) - ord('a')] > 0:
                tMap[ord(aChar) - ord('a')] -= 1
            else:
                return False
        return True


if __name__ == "__main__":
    s, t = "anagram", "nagaram"
    res = Solution().isAnagram(s, t)
    print(res)
