class Solution:
    # O(n)
    def frequencySort(self, s: str) -> str:
        freMap = {}
        ret = ''
        for aChar in s:
            if aChar in freMap:
                freMap[aChar] += 1
            else:
                freMap[aChar] = 1
        # print(freMap)
        for k in sorted(freMap, key=freMap.__getitem__, reverse=True):
            ret += k * freMap[k]
        return ret


if __name__ == "__main__":
    s = "tree"
    res = Solution().frequencySort(s)
    print(res)
