#
# @lc app=leetcode.cn id=122 lang=python3
#
# [122] 买卖股票的最佳时机 II
#
from typing import List

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxpro = 0
        for i in range(len(prices) - 1):
            maxpro += max(0, prices[i+1] - prices[i])
        return maxpro
# @lc code=end

if __name__ == "__main__":
    prices = [0,1,1,5,3,6,4]
    res = Solution().maxProfit(prices)
    print(res)