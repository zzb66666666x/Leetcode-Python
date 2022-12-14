# https://leetcode.com/problems/house-robber/
# method1: O(n^2) time
# class Solution:
#     def rob(self, nums: List[int]) -> int:
#         if len(nums) == 1:
#             return nums[0]
#         dp = [0 for _ in range(len(nums))]
#         dp[0] = nums[0]
#         dp[1] = nums[1]
#         maxval = max(dp[0], dp[1])
#         for i in range(2, len(nums)):
#             tmp = 0
#             for j in range(i-1):
#                 tmp = max(tmp, dp[j])
#             dp[i] = tmp + nums[i]
#             maxval = max(dp[i], maxval)
#         return maxval
    
# method2: optimize to O(n) time
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        dp = [0 for _ in range(len(nums))]
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], dp[i-2]+nums[i])
        return dp[len(nums)-1]
