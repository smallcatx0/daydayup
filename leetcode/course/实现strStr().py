class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        needLen = len(needle)
        hayLen = len(haystack)
        if needLen == 0:
            return 0
        if needLen > hayLen:
            return -1
        for i in range(hayLen - needLen + 1) :
            # print(haystack[i: i + needLen])
            if haystack[i: i + needLen] == needle:
                return i
        return -1


if __name__ == "__main__":
    str = "hello"
    need = 'll'
    res = Solution().strStr(str, need)
    print(res)