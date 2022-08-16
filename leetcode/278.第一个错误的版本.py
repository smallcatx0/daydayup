#
# @lc app=leetcode.cn id=278 lang=python3
#
# [278] 第一个错误的版本
#
t = 1702766719
# @param version, an integer
# @return an integer
def isBadVersion(version):
    return t <= version
# @lc code=start
# The isBadVersion API is already defined for you.

class Solution:
    # c = 0
    # 94.54%(32ms)  20.26% (14.9MB)
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 二分部查找法
        if isBadVersion(1):
            return 1
        l,r = 1, n
        mid = l + (r - l) // 2
        while mid <= r:
            bad = isBadVersion(mid)
            if bad:
                if not isBadVersion(mid - 1):
                    return mid
                else:
                    r = mid - 1
            else:
                if isBadVersion(mid + 1):
                    return mid + 1
                else:
                    l = mid + 1
            mid = l + (r - l) // 2
            # self.c += 1
        
# @lc code=end

if __name__ == "__main__":
    s = Solution()
    res = s.firstBadVersion(2126753390)
    print(res)
    print(s.c)