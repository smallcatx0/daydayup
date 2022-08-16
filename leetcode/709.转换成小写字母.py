#
# @lc app=leetcode.cn id=709 lang=python3
#
# [709] 转换成小写字母
#

# @lc code=start
class Solution:
    # 94.97 %(32 ms) 21.12 %(14.9 MB)
    def toLowerCase(self, str: str) -> str:
        res = []
        for i in range(len(str)):
            ac = ord(str[i])
            if ac >= 65 and ac <= 90:
                res.append(chr(ac + 32))
            else:
                res.append(str[i])
        return ''.join(res)
# @lc code=end

if __name__ == "__main__":
    s = "aAaSaa"
    res = Solution().toLowerCase(s)
    print(res)