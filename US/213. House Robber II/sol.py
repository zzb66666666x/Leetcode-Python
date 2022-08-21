# https://leetcode.com/problems/house-robber-ii/
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        # return max(self.robLinear(nums, 0, len(nums)-2), self.robLinear(nums, 1, len(nums)-1), self.robLinear(nums, 1, len(nums)-2))
        return max(self.robLinear(nums, 0, len(nums)-2), self.robLinear(nums, 1, len(nums)-1))
        
    def robLinear(self, nums, begin, end):
        length = end-begin+1
        if length == 1:
            return nums[begin]
        dp = [0 for _ in range(length)]
        dp[0] = nums[begin]
        dp[1] = max(dp[0], nums[begin+1])
        for i in range(2, length):
            dp[i] = max(nums[i+begin]+dp[i-2], dp[i-1])
        return dp[length-1]
