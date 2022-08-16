class Solution:
    def reverseVowels(self, s: str) -> str:
        if len(s) <= 1:
            return s
        s = list(s)
        vIndex = []
        v = ('a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U')
        for i in range(0, len(s)):
            if s[i] in v:
                # print(s[i])
                vIndex.append(i)
        indexLen = len(vIndex)
        mid = (indexLen) // 2
        for i in range(0, mid):
            j = indexLen - i - 1
            # print(vIndex[i], vIndex[j])
            s[vIndex[i]], s[vIndex[j]] = s[vIndex[j]], s[vIndex[i]]
        return ''.join(s)

if __name__ == "__main__":
    s = 'ai'
    res = Solution().reverseVowels(s)
    print(res)
