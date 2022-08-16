#
# @lc app=leetcode.cn id=917 lang=python3
#
# [917] 仅仅反转字母
#

# @lc code=start
class Solution:
    # 15.32 %(48ms)  96.1%(14.6MB)
    def reverseOnlyLetters(self, S: str) -> str:
        # 找出并过滤所有-的索引
        ix = []
        res = []
        for i in range(len(S)):
            if S[i].isalpha():
                res.append(S[i])
            else:
                ix.append((i, S[i]))
        res.reverse()
        for (i,s) in ix:
            res.insert(i, s)
        return ''.join(res)
# @lc code=end
if __name__ == '__main__':
    cases = [
        {'in': ("a-bC-dEf-ghIj"), 'out': "j-Ih-gfE-dCba"},
        {'in': ("Test1ng-Leet=code-Q!"), 'out': "Qedo1ct-eeLg=ntse-T!"}
    ]
    for one in cases:
        res = Solution().reverseOnlyLetters(one['in'])
        if res != one['out']:
            print(one["in"])
