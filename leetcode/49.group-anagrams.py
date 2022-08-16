from typing import *


class Solution:
    # O(n*mlogm) 120ms 95.4%
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 字典序 再比较
        ret = []
        addMap = {}
        for aStr in strs:
            cpStr = ''.join(sorted(aStr))
            if cpStr in addMap:
                ret[addMap[cpStr]].append(aStr)
            else:
                ret.append([aStr])
                addMap[cpStr] = len(ret) - 1
        return ret


if __name__ == "__main__":
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    res = Solution().groupAnagrams(strs)
    # res = strs.append("qqq")
    print(res)
