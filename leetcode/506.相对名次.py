#
# @lc app=leetcode.cn id=506 lang=python3
#
# [506] 相对名次
#
from typing import *

# @lc code=start
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        res = []
        mc = {'1': "Gold Medal", '2':'Silver Medal', '3':'Bronze Medal'}
        sortedS = score[:]
        sortedS.sort(reverse=True)
        m, i = {}, 0
        for one in sortedS:
            m[one] = str(i + 1)
            i+=1
        for one in score:
            j = m[one] 
            if j in mc.keys():
                res.append(mc[j])
            else:
                res.append(str(j))
        return res
# @lc code=end

if __name__ == '__main__':
    arr = [1,2,3,4,5] # [,,,2,]
    # arr = [1,2] # [,,,2,]
    res = Solution().findRelativeRanks(arr)
    print(res)