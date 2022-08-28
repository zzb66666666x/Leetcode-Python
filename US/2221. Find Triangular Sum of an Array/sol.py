# https://leetcode.com/problems/find-triangular-sum-of-an-array/
class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        numlen = len(nums)
        while numlen > 1:
            for i in range(numlen - 1):
                nums[i] = (nums[i] + nums[i+1])%10
            numlen -= 1
        return nums[0]
