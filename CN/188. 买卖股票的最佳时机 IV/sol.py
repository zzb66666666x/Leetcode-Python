# https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-iv/
class state:
    def __init__(self, a, b):
        self.buy = a
        self.sell = b

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if len(prices)==0 or k==0:
            return 0
        states = []
        for i in range(k):
            states.append(state(-prices[0], 0))
        for i in range(1,len(prices)):
            for j in range(k):
                if j==0:
                    states[j].buy = max(states[j].buy, -prices[i])
                else:
                    states[j].buy = max(states[j].buy, states[j-1].sell-prices[i])
                states[j].sell = max(states[j].sell, states[j].buy+prices[i])
        return states[k-1].sell
