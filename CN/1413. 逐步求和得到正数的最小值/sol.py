
# https://leetcode.cn/problems/minimum-value-to-get-positive-step-by-step-sum/
class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        # sumval = [0 for _ in range(len(nums))]
        curval = 0
        minval = 10000
        for i in range(len(nums)):
            curval += nums[i]
            minval = curval if curval<minval else minval
        # print(minval)
        # return max(1-minval, 1)
        return 1-minval if 1-minval > 0 else 1
