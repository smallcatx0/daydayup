#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i, j = 0, -1  # 滑动窗口
        searchMap = {}
        maxLen = 0
        while j < len(s) - 1:
            # print(searchMap)
            if s[j + 1] in searchMap:
                del searchMap[s[i]] # 数据出队
                i += 1
            else:
                searchMap[s[j + 1]] = 1
                j += 1
                maxLen = max(maxLen, j - i + 1)
        return maxLen
# @lc code=end

if __name__ == "__main__":
    res = Solution().lengthOfLongestSubstring('pwwkew')
    print(res)