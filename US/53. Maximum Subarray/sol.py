# https://leetcode.com/problems/maximum-subarray/
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        dp = [0 for i in range(len(nums))]
        dp[0] = nums[0]
        maxval = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(dp[i-1]+nums[i], nums[i])
            if dp[i] > maxval:
                maxval = dp[i]
        return maxval
