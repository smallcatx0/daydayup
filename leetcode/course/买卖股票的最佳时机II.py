""" 
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。

设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。

注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）
"""
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        has = None
        for i in range(len(prices) - 1):
            if prices[i] < prices[i + 1] and has == None:
                # 买 
                has = prices[i]
            if prices[i] > prices[i + 1] and has != None:
                # 卖
                profit += prices[i] - has
                has = None
        if has != None and has < prices[i + 1]:
            # 卖
            profit += prices[i + 1] - has
        return profit

if __name__ == "__main__":
    prices = [7,1,4,6,8,1,3]
    prices = [1,2,3,2,1]
    res = Solution().maxProfit(prices)
    print(res)
