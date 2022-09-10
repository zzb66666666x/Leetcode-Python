# https://leetcode.cn/problems/best-time-to-buy-and-sell-stock/
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # dp = [0 for _ in range(len(prices))]
        # dp[0] = 0
        first = 0
        second = 0
        maxval = 0
        for i in range(1,len(prices)):
            second = max(0, first + prices[i] - prices[i-1])
            maxval = max(maxval, second)
            first = second
        return maxval
