# https://leetcode.com/problems/jump-game-vi/
# method1: ordered queue
from collections import deque

class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [-2000000000 for _ in range(n)]
        dp[0] = nums[0]
        q = deque()
        q.append(0)
        for i in range(1, n):
            while len(q)>0 and q[0] + k < i:
                q.popleft()
            dp[i] = nums[i] + dp[q[0]]
            while len(q)>0 and dp[i] > dp[q[-1]]:
                q.pop()
            q.append(i)
        return dp[n-1]
