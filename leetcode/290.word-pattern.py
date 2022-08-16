
class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        strArr = str.split(' ')
        if len(strArr) != len(pattern):
            return False
        pMap = {}
        wordSet = set()
        for i in range(0, len(pattern)):
            if pattern[i] not in pMap:
                pMap[pattern[i]] = strArr[i]
                if strArr[i] in wordSet:
                    return False
                wordSet.add(strArr[i])
                continue
            if pMap[pattern[i]] != strArr[i]:
                return False
        return True


if __name__ == "__main__":
    pattern, str = 'abba', "dog dog dog dog"
    res = Solution().wordPattern(pattern, str)
    print(res)
