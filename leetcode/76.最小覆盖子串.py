class Solution:
    # O(n*m)
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t) or len(s) == 0:
            return ''
        if s == t:
            return s
        l, r = 0, -1  # [l..r] 为s包含t的子串
        searchMap = {}
        minSubStr = s + 'a'
        for c in t:
            if c in searchMap:
                searchMap[c] += 1
            else:
                searchMap[c] = 1
        judSet = set(t)
        # 最小覆盖子窜一定以t中的某个字母开头
        while r < len(s) - 1 and l < len(s):
            if r < l:  # 滑动窗口为空时，先找左边界
                if s[l] in searchMap:
                    r = l
                    searchMap[s[l]] -= 1
                    if searchMap[s[l]] <= 0:
                        judSet.remove(s[l])
                else:
                    l += 1  # 左边界右移动
                    r = l - 1  # 保持滑动窗口内容为空
                    continue
            if len(judSet) > 0:  # 滑动窗口内未包含完-》继续扩宽
                r += 1
                if s[r] in searchMap:
                    searchMap[s[r]] -= 1
                    if searchMap[s[r]] == 0:
                        judSet.remove(s[r])
                        if len(judSet) == 0 and len(minSubStr) > len(s[l:r + 1]):
                            minSubStr = s[l: r + 1]
            else:  # 滑动窗口内包含要查找的字符-》收缩滑动窗口
                # 找到一个结果
                # print('suss:', s[l: r + 1])
                if len(minSubStr) > len(s[l:r + 1]):
                    minSubStr = s[l: r + 1]
                # 左边界收缩,移除边界的元素从新放入查找表中
                searchMap[s[l]] += 1
                if searchMap[s[l]] > 0:
                    judSet.add(s[l])
                l += 1
                # 找到下一个以t中的某个字母开头的位置
                while l < len(s) and s[l] not in searchMap:
                    l += 1
                # print('next:', s[l:r + 1], judSet)
        if len(minSubStr) > len(s):
            return ''
        else:
            return minSubStr

    def minWindow2(self, s: str, t: str) -> str:
        if len(s) < len(t) or len(s) == 0:
            return ''
        if s == t:
            return s
        l, r = 0, -1  # [l..r] 为s包含t的子串
        searchMap = {}
        minSubStr = s
        for c in t:
            if c in searchMap:
                searchMap[c] += 1
            else:
                searchMap[c] = 1
        judSet = set(t)
        while 1:
            # 最小覆盖子串一定是t中的字母开头的
            while s[l] not in searchMap:
                l += 1
                if l > len(s) - 1:
                    break
            # 开始找覆盖子串
            while len(judSet) > 0:
                r += 1
                if r > len(s) - 1:
                    break
                if s[r] in searchMap:
                    searchMap[s[r]] -= 1
                    if searchMap[s[r]] == 0:
                        judSet.remove(s[r])
            # 找到了
            print("suss:", s[l:r + 1])
            if len(minSubStr) > len(s[l:r + 1]):
                minSubStr = s[l: r + 1]
            # 缩小滑动窗口
            searchMap[s[l]] += 1
            if searchMap[s[l]] > 0:
                judSet.add(s[l])
            l += 1
        return 0


def test():
    test = [
        {"s": "QERADOBECODEBANC", 't': "ABC", 'res': 'BANC'},
        {"s": "a", 't': "a", 'res': 'a'},
        {"s": "ab", 't': "b", 'res': 'b'},
        {"s": "aa", 't': "aa", 'res': 'aa'},
        {"s": "abc", 't': "ac", 'res': 'abc'},
        {"s": "bbc", 't': "bc", 'res': 'bc'}
    ]
    for one in test:
        res = Solution().minWindow(one['s'], one['t'])
        print(res)
        assert one['res'] == res


if __name__ == "__main__":
    s, t = "QERADOBECODEBANC", "ABC"
    # s, t = "QWERT", "ABC"
    res = Solution().minWindow2(s, t)
    print(res)
