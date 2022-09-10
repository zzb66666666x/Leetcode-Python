# https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-ii/
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prev = prices[0]
        profit = 0
        for i in range(1, len(prices)):
            if prices[i]>prev:
                profit += (prices[i] - prices[i-1])
            prev = prices[i]
        return profit
