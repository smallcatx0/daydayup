#
# @lc app=leetcode.cn id=434 lang=python3
#
# [434] 字符串中的单词数
#

# @lc code=start
class Solution:
    # 82.16 % (36 ms) s 87.22 % (14.7 MB)
    def countSegments(self, s: str) -> int:
        pre,curr = 0, 0
        count = 0
        for c in s:
            pre = curr
            if c == ' ':
                curr = 0
            else:
                curr = 1
            if pre == 0 and curr == 1:
                count += 1
        return count
# @lc code=end

if __name__ == '__main__':
    s = "Hello, my    name is   Jo hn   "
    res = Solution().countSegments(s)
    print(res)