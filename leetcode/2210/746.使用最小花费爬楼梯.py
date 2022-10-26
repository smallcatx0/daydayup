#! python3

'''

https://leetcode.cn/problems/min-cost-climbing-stairs/
'''

from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        curr = pre = 0
        for i in range(2,n+1): 
            next = min(curr + cost[i-1], pre+cost[i-2])
            pre, curr = curr, next
        return curr


if __name__ == '__main__':
    cost = [10,15,20]
    ret = Solution().minCostClimbingStairs(cost)
    print(ret)