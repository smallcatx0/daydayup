#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start

class Solution:
    def isValid1(self, s):
        z = []
        res = True
        for x in s:
            if x in ('{', '[', '('):
                z.append(x)
            if x == ']':
                res = self.popList(z, '[')
            if x == '}':
                res = self.popList(z, '{')
            if x == ')':
                res = self.popList(z, '(')
            if res is False:
                return False
        if len(z) != 0:
            return False
        return True

    def popList(self, z, c):
        if len(z) == 0:
            return False
        if z.pop() == c:
            return True
        return False

    def isValid(self, s):
        matchMap = {'}': '{', ']': '[', ')': '('}
        stack = []
        for ch in s:
            if ch not in matchMap:
                stack.append(ch)
            else:
                if len(stack) == 0:
                    return False
                if matchMap[ch] != stack.pop():
                    return False
        return len(stack) == 0
# @lc code=end


if __name__ == "__main__":
    s = '{{({})}}'
    s = '['
    res = Solution().isValid(s)
    print(res)
