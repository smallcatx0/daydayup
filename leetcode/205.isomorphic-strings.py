class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        mapping = {}
        valueSet = set()
        for i in range(0, len(s)):
            if s[i] not in mapping:
                if t[i] in valueSet:
                    return False
                mapping[s[i]] = t[i]
                valueSet.add(t[i])
                continue
            if mapping[s[i]] != t[i]:
                return False
        return True


if __name__ == "__main__":
    s, t = "egbg", "adod"
    res = Solution().isIsomorphic(s, t)
    print(res)
