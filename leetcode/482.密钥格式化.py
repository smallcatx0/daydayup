#
# @lc app=leetcode.cn id=482 lang=python3
#
# [482] 密钥格式化
#

# @lc code=start
class Solution:
    # 50.56 % (80ms) 91.01%(18.2 MB)
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        ls,t = len(S),K
        res = ''
        for i in range(ls-1, -1, -1):
            if S[i] != '-':
                res = S[i].upper() + res
                t -= 1
                if t == 0:
                    t = K
                    res = '-' + res
        if len(res) != 0 and res[0] == '-':
            return res[1:]
        return res
# @lc code=end

if __name__ == "__main__":
    S,K = "5FA3Z-2e-9-w", 3
    res = Solution().licenseKeyFormatting(S, K)
    print(res)
