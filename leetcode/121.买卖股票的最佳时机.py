#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
#
from typing import List


# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        minPirce, maxPro = prices[0], 0
        for one in prices[1:]:
            minPirce = min(one,minPirce)
            maxPro = max(one - minPirce, maxPro)
        return maxPro


# @lc code=end

if __name__ == "__main__":
    prices = [7,1,5,3,6,4]
    res = Solution().maxProfit(prices)
    print(res)