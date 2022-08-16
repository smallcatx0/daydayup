from typing import *


class Solution:
    # Timeout
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ret = []
        sLen = len(s)
        serLen = len(p)
        for i in range(0, sLen - serLen + 1):
            serkey = list(p)
            for j in range(0, serLen):
                # print(i, j, s[i+j])
                if s[i + j] in serkey:
                    serkey.remove(s[i + j])
                else:
                    break
            if len(serkey) == 0:
                ret.append(i)
        return ret

    # O(n*m)
    # 滑动窗口思路
    def findAnagrams1(self, s: str, p: str) -> List[int]:
        sLen, pLen = len(s), len(p)
        if sLen < pLen:
            return []
        ret = []
        l, r = 0, -1  # [l..r] 区间为p中的 部分-> 全部 字符
        serchList = list(p)  # TODO 这里用map效率会更高
        while r < sLen - 1:
            print(l, r, s[r + 1], serchList)
            if s[r + 1] in serchList:  # 如果右边的下一位s[r+1]在查找数组中
                r += 1  # 则将其加入区间中
                serchList.remove(s[r])  # 并消耗掉此字符
                if len(serchList) == 0:  # 如果查找数组为空则说明区间中为p的异构符
                    ret.append(l)  # 将区间左边界地址存入结果集
                    serchList.append(s[l])  # 区间收缩,并将左边移除的字符重新加入查找数组中
                    l += 1
            else:  # 如果右边的下一位不符合要求，分两种情况
                if s[r + 1] in p:  # 下一位依然在p字符串中
                    # 则说明区间中此字符超过了p中的量
                    serchList.append(s[l])  # 缩小区间，直到能将此字符包含进区间里
                    l += 1
                else:  # 右边下一位不在字符串p中，则包含此字符的一定不是p的异构符
                    serchList = list(p)
                    r += 1  # 直接将区间清零,左边界跳过此字符 ，并重置查找数组
                    l = r + 1
        return ret

    # 比解法1差
    def findAnagrams2(self, s: str, p: str) -> List[int]:
        ret = []
        if len(s) < len(p):
            return []
        pFreq = [0] * 26
        for one in p:
            pFreq[ord(one) - ord('a')] += 1
        sFreq = [0] * 26
        l, r = 0, 0
        while l <= len(s) - len(p):
            if r - l + 1 <= len(p):  # 扩宽滑动窗口
                sFreq[ord(s[r]) - ord('a')] += 1
                r += 1
                continue
            i = 0
            while i < 26 and sFreq[i] == pFreq[i]:
                i += 1
            if i == 26:
                ret.append(l)
            sFreq[ord(s[l]) - ord('a')] -= 1
            l += 1
        return ret

    def str2Map(self, s):
        serch = {}
        for one in s:
            if one in serch:
                serch[one] += 1
            else:
                serch[one] = 1
        return serch


if __name__ == "__main__":
    s, p = "abab", "ab"
    s, p = "cbaebabacd", "abc"
    s, p = "abacbabc", "abc"
    s, p = "abaacbabc", "abc"
    res = Solution().findAnagrams2(s, p)
    # res = Solution().findAnagrams1(s, p)
    # res = Solution().findAnagrams(s, p)
    print(res)
