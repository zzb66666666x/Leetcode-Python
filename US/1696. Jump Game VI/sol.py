# https://leetcode.com/problems/jump-game-vi/
# method1: priority queue
# class Solution:
#     def maxResult(self, nums: List[int], k: int) -> int:
#         dp = [0 for i in range(len(nums))]
#         dp[0] = nums[0]
#         q = [(-nums[0], 0)]
#         for i in range(1, len(nums)):
#             while q[0][1] + k < i:
#                 heapq.heappop(q)
#             val = nums[i] - q[0][0]
#             dp[i] = val
#             heapq.heappush(q, (-val, i))
#         return dp[len(nums)-1]
    
# method2: single order deque
class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        dp = [0 for i in range(len(nums))]
        n = len(nums)
        q = deque()
        dp[0] = nums[0]
        q.append(0)
        for i in range(1, n):
            while q[0] + k < i:
                q.popleft()
            val = dp[q[0]] + nums[i]
            dp[i] = val
            while len(q)>0 and dp[q[-1]] < val:
                q.pop()
            q.append(i)
        return dp[n-1]
