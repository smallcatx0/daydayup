#
# @lc app=leetcode.cn id=551 lang=python3
#
# [551] 学生出勤记录 I
#

# @lc code=start
class Solution:
    def checkRecord(self, s: str) -> bool:
        return s.count('A') <= 1 and 'LLL' not in s
        
    def checkRecord1(self, s: str) -> bool:
        At = 0
        Lmt = 0
        for c in s:
            if c == 'A':
                Lmt = 0
                At += 1
                if At > 1:
                    return False
            elif c == 'L':
                Lmt += 1
                if Lmt > 2:
                    return False
            else:
                Lmt = 0
        return True
# @lc code=end


if __name__ == "__main__":
    rec = 'LALL'
    res = Solution().checkRecord(rec)
    print(res)