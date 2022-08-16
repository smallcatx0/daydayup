from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ''
        prefixStr = ''
        i = 0
        tmp = ''
        while True:
            for str in strs:
                if i >= len(str):
                    return prefixStr
                if tmp == '':
                    tmp = str[i]
                    continue
                if tmp != str[i]:
                    return prefixStr
            prefixStr += tmp
            tmp = ''
            i += 1
        return ''

if __name__ == "__main__":
    strs = ["flower","flow","floight"]
    strs = ["dog","racecar","car"]
    strs = []
    res = Solution().longestCommonPrefix(strs)
    print(res)